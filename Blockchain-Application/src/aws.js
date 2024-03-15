//IF ENDPOINTs EXIST IN APP.JS, THEN DON'T USE THIS CODE
const express = require('express');
const AWS = require('aws-sdk');
const multer = require('multer');
const { v4: uuidv4 } = require('uuid');
const bodyParser = require('body-parser');
const contract = require('truffle-contract');
const MedicalRecordsJSON = require('../build/contracts/MedicalRecords.json');

// Initialize Express and middleware
const app = express();
app.use(bodyParser.json());

// Configure AWS SDK
AWS.config.update({
  accessKeyId: 'YOUR_ACCESS_KEY_ID',
  secretAccessKey: 'YOUR_SECRET_ACCESS_KEY',
  region: 'YOUR_REGION'
});

const s3 = new AWS.S3();
const upload = multer({ storage: multer.memoryStorage() });

// Connect to Ganache
const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545'));

// Create an instance of the smart contract
const medicalRecords = contract(MedicalRecordsJSON);
medicalRecords.setProvider(web3.currentProvider);

// Set the default account for transactions
web3.eth.getAccounts((err, accounts) => {
  if (err) throw err;
  web3.eth.defaultAccount = accounts[0];
  medicalRecords.defaults({ from: web3.eth.defaultAccount });
});


// AWS S3 Upload endpoint
app.post('/upload', upload, (req,res) => {
    const myFile = req.file.originalname.split('.');
    const fileType = myFile[myFile.length - 1];
    const key = req.body.fileName || uuidv4();

    if(!process.env.AWS_BUCKET_NAME) {
        console.error('AWS_BUCKET_NAME is not set in environment variables');
        return res.status(500).send({message: 'server error'});
    }
    
    const params = {
        Bucket: process.env.AWS_BUCKET_NAME,
        Key: key,
        Body: req.file.buffer
    };

    s3.upload(params, (error, data) => {
        if(error) {
            console.error('Error Uploading to AWS S3',error);
            return res.status(500).send({message: 'server error'});
        }
        res.status(200).send(data);
    });
});

// AWS S3 Download endpoint
app.get('/download/:key', (req, res) => {
    const params = {
        Bucket: process.env.AWS_BUCKET_NAME,
        Key: req.params.key
    };

    s3.getObject(params, (error, data) => {
        if(error) {
            console.error('Error Downloading from AWS S3',error);
            return res.status(500).send({message: 'Server error'});
        }

        console.log('Downloaded file name: ${req.params.key}');
        res.setHeader('Content-Type', data.ContentType);
        res.setHeader('Content-Disposition', 'attachment; filename="${req.params.key}"');
        res.send(data.Body);
    });
});

// Start the server
const port = process.env.PORT || 3001;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});


