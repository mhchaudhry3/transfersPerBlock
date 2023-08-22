from web3 import Web3;


w3 = Web3(Web3.HTTPProvider('insert node'))    
w3 = Web3(Web3.HTTPProvider('input node'))    
block_number = w3.eth.block_number
print(block_number)
number_of_transfers = 0
number_of_transactions = 0
print(block_number)
for x in range(block_number, block_number - 10000, -1):
    block = w3.eth.getBlock(x)
    for transaction_hash in block['transactions']:
        transaction = w3.eth.getTransaction(transaction_hash)
        if len(transaction['input']) == 2 or "0xa9059cbb" in transaction['input']:
            number_of_transfers += 1
        else:
            number_of_transactions += 1
    print(number_of_transactions, number_of_transfers, block_number - 1000, x )
    
print(number_of_transactions, number_of_transfers)
