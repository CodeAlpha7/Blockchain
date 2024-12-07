from web3 import Web3
import eth_abi


# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider("http://143.215.130.235:8545"))

# Define the contract address and ABI
contract_address = '0xc3E63CBBD5aa977D6465875796894eC18c0ce347'
abi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"constant":False,"inputs":[],"name":"KOTH_coup","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"KOTH_withdraw","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"coup_block","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel1v1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel_highroller","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"guess_the_number","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"mayor_voting","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"most_sent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"d","type":"uint256"}],"name":"pay_to_mine","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"richest","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"}]

# Create a contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# Define the caller address
caller = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"

# Get the state of the perm mapping for the caller
block_number = web3.eth.block_number
print(f'Block number: {block_number}')
