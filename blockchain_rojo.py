import hashlib
import json
from time import time


class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	# Create the genesis block
	self.new_block(previous_hash=1, proof=100)

def new_block(self, proof, previous_hash=None):
	"""
	Create a new Block in the Blockchain

	:param proof: <int> The proof given by the Proof of Work algorithm
	:param previous_hash: (Optional) <str> Hash of previous Block
	:return: <dict> New Block
	"""

	block = {
		'index': len(self.chain) + 1,
		'timestamp': time(),
		'transactions': self.current_transactions,
		'proof': proof,
		'previous_hash': previous_hash or self.hash(self.chain[-1]),
	}

	# Reset the current list of transactions
	self.current_transactions = []
	

	self.chain.append(block)
	return block

def new_transaction(self, sender, recipient, amount):
	"""
	Creates a new transaction to go into the next mined Block
	
	:param sender: <str> address of the Sender
	:param recipient: <str> address of the Recipient
	:param amount: <int> Amount
	:return: <int> The index of the Block that will hold this transaction
	"""

	self.current_transactions.append({
		'sender': sender,
		'recipient': recipient,
		'amount': amount,
	})

@staticmethod
def hash(block):
	"""
	Creates a SHA-256 hash of a Block

	:param block: <dict> Block
	:return: <str>
	"""

	#We must make sure the dictionary is ordered or we'll have inconsisitent hashes
	block_string = json.dumps(block, sort_keys=True).encode()
	return hashlib.sha256(block_string).hexdigest()
@property
def last_block(self):
	return self.chain[-1]
