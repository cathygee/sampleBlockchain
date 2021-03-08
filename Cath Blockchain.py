# Blockchain
"""
Created on Thu Mar  4 04:35:37 2021

@author: cathrineg
"""
import hashlib
import json

class Blockchain:

    def __init__(self):
        self.chain = []
        self.n = int(input('enter the number of employees to add to your blockchain :'))
        self.create_block(previous_hash = '0')
        print('the first block is:', self.chain)

    def create_block(self,previous_hash):
        block = {'index': len(self.chain) + 1,
                 'previous_hash': previous_hash,         
                 'name': input('enter name employee: '),
                 'surname': input('enter surname employee: ')}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]
   
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_block = block
            block_index += 1
        return True

blockchain = Blockchain()
n =  blockchain.n -1

def get_block():
    previous_block = blockchain.get_previous_block()
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(previous_hash)
    print('The new block :', block)
   
def get_chain():
    yourChain = blockchain.chain 
    lenth = len(blockchain.chain)
    print ( 'Your blockchain contains', yourChain  ) 
    print ('The lenth of the blockchain is:', lenth)

def show_chain():
            
    for i in range(0,n): 
        get_block()
        get_chain() 
show_chain()