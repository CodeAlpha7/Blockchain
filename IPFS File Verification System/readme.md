## IPFS File Verification System

### Requirements:
1. IPFS version 0.9.0
2. Truffle v5.11.5 (core: 5.11.5)
3. Ganache v7.9.1
4. Solidity - 0.8.13 (solc-js)
5. Node v16.15.1
6. Web3.js v1.10.0

### Steps to run:

1. Download zip file and unzip to any location
2. Ensure above requirements. Then, run:
```
npm install
```
3. Run local Ganache Instance via Ganache Desktop App. Note down network RPC URL.
4. Go to ```truffle-config.js```. Make sure ```networks``` --> ```development``` has the specified host and port as the RPC URL noted above from Ganache instance. Ensure in ```compilers``` --> ```solc: version``` is set to ```0.8.13```.
5. In powershell or CMD, to compile code and generate ABI and other artifacts, run:
```
truffle compile
```
6. Now, deploy smart contract to local ganache instance using:
```
truffle migrate --reset
```
7. Once deployment is successful, note down ```contract address```.
8. Within the ```app.js``` file, change existing contract address in code to above copied address from deployment. Also, make sure your connection to local ganache instance matches your deployed RPC URL.
9. In a new powershell or cmd window, setup local IPFS node using CLI, using:
```
ipfs daemon
```
10. Finally, run your express backend using:
```
node app.js
```
11. Now, access the UI by entering ```http://localhost:3000``` in your browser.
