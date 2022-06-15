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
        