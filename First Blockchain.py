# For the time stamp function
import datetime

# For calculating the hash to add thr digital fingerprints to the blocks
import hashlib

# For storing data in the blockchain
import _json

# We need to create the web app hence this flask. jsonify displays the blockchain
from flask import Flask, jsonify

# Let's begin

class Blockchain:
    # We're creating this first function to create the first block and set it to '0'
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    # Add further blocks to the chain 
    def create_block(self, proof, previous_hash) :
        block = {'index': len(self.chain) + 1,
                'timestamp' : str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash' : previous_hash}
        self.chain.append(block)
        return block

    # Display the previous block 
    def print_previous_block(self) :
        return self.chain[-1]

    # We want now to display the previous block
    def proof_of_work(self, previous_proof) :
        new_proof = 1
        check_proof = False 

        while check_proof is False :
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            )
            