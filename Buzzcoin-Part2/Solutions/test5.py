from web3 import Web3

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))

# Address of the smart contract
contract_address = "0xc3E63CBBD5aa977D6465875796894eC18c0ce347"
your_address = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"

# ABI of the smart contract
abi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"constant":False,"inputs":[],"name":"KOTH_coup","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"KOTH_withdraw","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"coup_block","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel1v1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel_highroller","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"guess_the_number","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"mayor_voting","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"most_sent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"d","type":"uint256"}],"name":"pay_to_mine","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"richest","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"}]

# Load the contract
contract = web3.eth.contract(address=contract_address, abi=abi)

# Iterate over the blocks
for block_number in range(80000, 900000):
    block = web3.eth.get_block(block_number)

    # Iterate over the transactions in the block
    for tx_hash in block['transactions']:
        try:
            tx = web3.eth.get_transaction(tx_hash)

            if tx['from'] == your_address:
                input_data = contract.decode_function_input(tx.input)
                print(f"Transaction Hash: {tx_hash.hex()}")
                print(f"Input data: {input_data}")
            
        except ValueError as e:
            print(f"Error decoding input data: {e}")
            continue

# Get the list of account addresses
# accounts = web3.eth.accounts

# # Iterate over each account and display its balance
# for account in accounts:
#     balance = web3.eth.get_balance(account)
#     print(f"Account: {account}")
#     print(f"Balance: {web3.from_wei(balance, 'ether')} ETH")


# most_sent_value = contract.functions.most_sent().call()
# most_ether = web3.from_wei(most_sent_value, 'ether')

# print("most_sent value:", most_ether)

