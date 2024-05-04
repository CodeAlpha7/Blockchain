const bodyParser = require("body-parser");
const ipfsAPI = require('ipfs-api');
const express = require('express');
const fileUpload = require('express-fileupload');
const fs = require('fs');
const { Web3 } = require('web3');

//connect to local ganache instance - to connect to a public blockchain enter its RPC URL here.
const web3 = new Web3('http://localhost:7545');     

// Connect to IPFS node running on localhost:5001
const ipfs = ipfsAPI('localhost', '5001', { protocol: 'http' });
const app = express();

//Reference ABI to interact with contract functions
const contractJSON = require('./build/contracts/StoreHash.json'); 
const abi = contractJSON.abi;
const ContractAddress = '0xA233d36fFb7b84D6ee240175Dc247d11579Bf7F3'; 

//creating new contract instance
const contract = new web3.eth.Contract(abi, ContractAddress);


// Configuration - using ejs as template language - sets view engine
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(fileUpload());

//function to store hash on blockchain using first account
const storeFileHashOnBlockchain = async (fileHash) => {
    try {
        // Call the contract's sendHash function
        const accounts = await web3.eth.getAccounts(); // Get available accounts
        const senderAddress = accounts[0]; // Use the first account
        const txReceipt = await contract.methods.sendHash(fileHash).send({ from: senderAddress });
        console.log('Transaction receipt:', txReceipt);
    } catch (error) {
        console.error('Error storing file hash on blockchain:', error);
    }
};

// Creating routes
app.get('/', (req, res) => {
    res.render('home');
});

app.post('/upload', (req, res) => {
    const file = req.files.file;
    const fileName = req.body.fileName;
    const filePath = 'files/' + fileName;

    // Download the file to our server
    file.mv(filePath, async (err) => {
        if (err) {
            console.log('Error: failed to download file');
            return res.status(500).send(err);
        }

        // Call addFile() with correct fileName and filePath - returns promise
        const fileHash = await addFile(fileName, filePath);

        //store file hash on blockchain
        await storeFileHashOnBlockchain(fileHash);

        // Once we upload to IPFS, get hash and upload to blockchain, we can delete the file
        fs.unlink(filePath, (err) => {
            if (err) console.log(err);
        });

        // Render page with right parameters
        res.render('upload', { fileName, fileHash });
    });
});

// Function that adds file to IPFS - need access to filesystem
const addFile = async (fileName, filePath) => {
    const file = fs.readFileSync(filePath);
    const fileAdded = await ipfs.add(file);
    const fileHash = fileAdded[0].hash; // Hash - content identifier

    return fileHash;
};

app.listen(3000, () => {
    console.log('Server is listening on port 3000');
});
