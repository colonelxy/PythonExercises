# For the time stamp function
import datetime

# For calculating the hash to add thr digital fingerprints to the blocks
import hashlib

# For storing data in the blockchain
import json

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
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000' :
                check_proof = True 
            else :
                new_proof += 1
        return new_proof

    def hash(self, block) :
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def chain_valid(self, chain) :
        previous_block =  chain[0]
        block_index = 1

        while block_index < len(chain) :
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block) :
                return False 

            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:5] != '00000' :
                return False 
            previous_block = block
            block_index +=1
        return True 
# Creating the web app using flask 
app = Flask(__name__)


#  Create the object of the class Blockchain
blockchain = Blockchain()

# Mining a new block 
@app.route('/mine_block', methods = ['GET'])
def mine_block() :
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message' : 'A block is MINED', 'index' : block['index'], 'timestamp' : block['timestamp'], 'proof' : block['proof'], 'previous_hash' : block['previous_hash']}

    return jsonify(response), 200

# Display blockchain in json format 
@app.route('/get_chain', methods=['GET'])
def display_chain() :
    response = {'chain' : blockchain.chain,     'length' : len(blockchain.chain)}
    return jsonify(response), 200

# Check validity of the blockchain 
@app.route('/valid', methods=['GET'])
def valid() :
    valid = blockchain.chain_valid(blockchain.chain)
    if valid:
        response = {'message' : 'The blockchain is valid.'}
    else:
            response = {'message': 'The blockchaini s not valid.'}
            return jsonify(response), 200



# Run the flask locally
app.run(host='0.0.0.0', port=5000)





    
    