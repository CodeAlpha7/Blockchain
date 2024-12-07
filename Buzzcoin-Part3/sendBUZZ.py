from web3 import Web3
import eth_abi

# Connect to the Ethereum node
web3 = Web3(Web3.HTTPProvider("http://143.215.130.235:8545"))

# Define the caller address and private key
caller = "0x1D95c52ec00fce1c4E86f56a26Df021D96451A90"
private_key = "003cb618783a20afec4b5eb7911545c58d9d67be49ca93280a1bac05052678f8"

nonce = web3.eth.get_transaction_count(caller)

recipient_address = "0x17ce8932E45dc4fe6Ef573829d0D506b679e24F4"

amount_ether = 20
amount_wei = web3.to_wei(amount_ether, 'ether')

Chain_id = web3.eth.chain_id

transaction = {
    'chainId': Chain_id,
    'to': recipient_address,
    'value': amount_wei,
    'gas': 1000000,  # Gas limit (adjust as needed)
    'gasPrice': web3.to_wei('1', 'gwei'),  # Gas price in Wei (adjust as needed)
    'nonce': nonce,
}

signed_tx = web3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Check 3")

# Send transaction
send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("Check 4")

# Wait for transaction receipt
tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)

print(f"Transaction hash: {send_tx.hex()}")