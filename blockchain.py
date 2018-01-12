import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactiions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        
        block= {
            'index' = len(self.chain) + 1,
            'timestamp' = time(),
            'transactions' = self.current_transactiions,
            'proof' = proof,
            'previous_hash' = previous_hash or self.hash(self.chain[-1]),
            }

        self.current_transactiions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recepient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactiions.append({
            'sender': sender,
            'recepient': recepient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
        #adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        #hashes a block
        pass

    @property
    def last_block(self):
        #returns the last block in the chain
        pass        