# from web3 import Web3

# # Connect to the blockchain
# web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))

# # Get the latest block number
# latest_block_number = web3.eth.block_number

# # Get the last 100 blocks to print
# start_block_number = max(0, latest_block_number - 99)  # Ensure not to go below block 0

# # Iterate over the last 100 blocks
# for block_number in range(start_block_number, latest_block_number + 1):
#     # Retrieve the block
#     block = web3.eth.get_block(block_number)

#     # Check if the block has transactions
#     if block['transactions']:
#         print(f"Block Number: {block_number}")
#         print("Transactions:")
        
#         # Print transactions in the block
#         for tx_hash in block['transactions']:
#             transaction = web3.eth.get_transaction(tx_hash)
#             print(transaction)
#         print()

from web3 import Web3

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))

# Number of transactions to retrieve
num_transactions_to_retrieve = 10000

# Initialize variables
transactions_collected = 0
current_block_number = web3.eth.block_number

# Iterate over blocks starting from the latest block
while transactions_collected < num_transactions_to_retrieve and current_block_number >= 0:
    # Retrieve the block
    block = web3.eth.get_block(current_block_number)

    # Check if the block has transactions
    if block['transactions']:
        # Print block number
        print(f"Block Number: {current_block_number}")
        print("Transactions:")

        # Iterate over transactions in the block
        for tx_hash in block['transactions']:
            # Retrieve transaction
            transaction = web3.eth.get_transaction(tx_hash)
            print(transaction)

            # Increment the count of collected transactions
            transactions_collected += 1

            # Check if we have collected enough transactions
            if transactions_collected >= num_transactions_to_retrieve:
                break

        print()

    # Move to the previous block
    current_block_number -= 1

# If we couldn't collect enough transactions, inform the user
if transactions_collected < num_transactions_to_retrieve:
    print(f"Only {transactions_collected} transactions found in the last {num_transactions_to_retrieve} transactions.")