from web3 import Web3
import json

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))

# Your Ethereum address
your_address = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"

# ABI of the smart contract
contract_abi = [
    {"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},
    {"payable":True,"stateMutability":"payable","type":"fallback"},
    {"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},
    {"constant":True,"inputs":[],"name":"logmask","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
    {"constant":True,"inputs":[],"name":"mask","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},
    {"constant":False,"inputs":[],"name":"problem1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},
    {"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"problem2","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},
    {"constant":False,"inputs":[],"name":"problem3","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},
    {"constant":False,"inputs":[],"name":"problem4","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},
    {"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"problem5","outputs":[],"payable":True,"stateMutability":"payable","type":"function"}
]

# Load the contract
contract = web3.eth.contract(abi=contract_abi)

# Iterate over the blocks
for block_number in range(web3.eth.block_number, 0, -1):  # Iterate from latest block to block 0
    block = web3.eth.get_block(block_number)

    # Fetch logs for the block
    logs = web3.eth.get_logs({'fromBlock': block_number, 'toBlock': block_number, 'address': your_address})
    
    # Iterate over the transactions in the block
    for tx_hash in block['transactions']:
        tx = web3.eth.get_transaction(tx_hash)

        # Check if your address is involved in the transaction as a sender or receiver
        if tx['from'] == your_address or tx['to'] == your_address:
            print(f"Transaction Hash: {tx_hash}")
            print(f"From: {tx['from']}")
            print(f"To: {tx['to']}")
            print(f"Value: {web3.from_wei(tx['value'], 'ether')} ETH")
            print()

    # Iterate over the logs in the block
    for log in logs:
        if log['address'].lower() == your_address.lower():
            # Decode the log data using contract ABI
            event = contract.events.LogMask().processLog(log)
            if event:
                print(f"Transaction Hash: {log['transactionHash'].hex()}")
                print(f"From: {log['topics'][1].hex()}")
                print(f"To: {your_address}")
                print(f"Value: {event[0]['args']['']}")
                print()