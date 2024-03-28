# 1. Import web3.py
from web3 import Web3

# 2. Create web3.py provider
web3 = Web3(Web3.HTTPProvider("http://143.215.130.235:8545")) # Insert your RPC URL here

address_from = '0x1D95c52ec00fce1c4E86f56a26Df021D96451A90'

# 3. Fetch balance data
balance_from = web3.from_wei(
    web3.eth.get_balance(Web3.to_checksum_address(address_from)), "ether"
)


print(f"The balance of { address_from } is: { balance_from } DEV")