from web3 import Web3
import eth_abi

# 2. Create web3.py provider
web3 = Web3(Web3.HTTPProvider("http://143.215.130.235:8545")) # Insert your RPC URL here

caller = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"
private_key = "003cb618783a20afec4b5eb7911545c58d9d67be49ca93280a1bac05052678f8"

nonce = 4

contract_address = '0xd7111d1C305B39E327d1f1Ba7e7D0cb57f26Ff09'

abi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"logmask","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"mask","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"problem1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"problem2","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"problem3","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"problem4","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"problem5","outputs":[],"payable":True,"stateMutability":"payable","type":"function"}]

# // print(f"Making a call to contract at address: { contract_address }")

# 4. Create contract instance
contract = web3.eth.contract(address=contract_address, abi=abi)

# encoded = eth_abi.encode(['uint256', 'address'], [nonce, contract_address])
# hash_value = web3.solidity_keccak(['bytes'], [encoded])
hash_value = web3.solidity_keccak(['uint256', 'address'], [nonce, contract_address])
print(f'The hash is: {hash_value.hex()}')
