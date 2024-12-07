from web3 import Web3

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))

# Your Ethereum address
your_address = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"

# Iterate over the blocks
for block_number in range(web3.eth.block_number, 0, -1):  # Iterate from latest block to block 0
    block = web3.eth.get_block(block_number)

    # Iterate over the transactions in the block
    for tx_hash in block['transactions']:
        tx = web3.eth.get_transaction(tx_hash)

        # Check if your address is involved in the transaction
        if tx['from'] == your_address or tx['to'] == your_address:
            print(f"Transaction Hash: {tx_hash}")
            print(f"From: {tx['from']}")
            print(f"To: {tx['to']}")
            print(f"Value: {web3.from_wei(tx['value'], 'ether')} ETH")
            print()