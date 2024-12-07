# Import necessary libraries
from web3 import Web3
import eth_abi

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider("http://143.215.130.235:8545"))

# Define the caller address and private key
caller = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"
private_key = "003cb618783a20afec4b5eb7911545c58d9d67be49ca93280a1bac05052678f8"

nonce = web3.eth.get_transaction_count(caller)

# Define the contract address and ABI
contract_address = '0xc3E63CBBD5aa977D6465875796894eC18c0ce347'
abi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"constant":False,"inputs":[],"name":"KOTH_coup","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"KOTH_withdraw","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"coup_block","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel1v1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel_highroller","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"guess_the_number","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"mayor_voting","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"most_sent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"d","type":"uint256"}],"name":"pay_to_mine","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"richest","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"}]

print(f"Making a call to contract at address: { contract_address }")

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)
print("created contract instance successfully")

# Generate nonce and other transaction parameters
block_number = web3.eth.block_number
block_number = block_number + 1

print("Block Number: ", block_number)
encoded1 = eth_abi.encode(['address'], [caller])
encoded2 = eth_abi.encode(['uint256'], [block_number])
temp = web3.solidity_keccak(['bytes'], [encoded1])
temp = web3.solidity_keccak(['bytes','bytes'], [temp, encoded2])
temp = web3.solidity_keccak(['bytes','bytes'], [temp, temp])
answer = int.from_bytes(temp, byteorder='big') % 100
print("Nonce: ", answer)


Chain_id = web3.eth.chain_id

transaction = {'chainId': Chain_id, 'from': caller, 'nonce': nonce, 'gas': 5000000, 'gasPrice': web3.to_wei(5, 'gwei'),  'value': web3.to_wei(1, 'ether') }
print("Check 1")
# Call your function
call_function = contract.functions.guess_the_number(answer).build_transaction(transaction)
print("Check 2")

# Sign transaction
signed_tx = web3.eth.account.sign_transaction(call_function, private_key=private_key)
print("Check 3")

# Send transaction
send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("Check 4")

# Wait for transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx, timeout=500)
print("Check 5")
# print(tx_receipt) # Optional

print(f"Transaction hash: {send_tx.hex()}")
print("Block Number: ", web3.eth.block_number)
