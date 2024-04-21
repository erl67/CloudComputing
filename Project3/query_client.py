import hashlib
from blockchain import Blockchain
from db_provider import Server
from data_owner import DataOwner
import merkletools
from adv_client import MaliciousClient

# This class serves as a query client and also performs verification
class QueryClient:
    def __init__(self, server, blockchain):
        self.server = server
        self.blockchain = blockchain

    # perform query to server
    def query_by_key(self, key):
        return self.server.get_data(key)

    # get proof from server's merkle tree
    def retrieve_verification_path_by_tree(self, key_index):
        return self.server.get_merkle_proof(key_index)

    # get merkle root from blockchain
    def retrieve_root_from_blockchain(self):
        return self.blockchain.get_merkle_root()

    # Query clients issue query verifications
    def query_verification(self, retrieved_value, proofs, root_from_contract):
        if (retrieved_value is None) or (proofs is None):
            return False

        hash_value = hashlib.sha256(retrieved_value.encode()).hexdigest()

        temp_tree = merkletools.MerkleTools()
        temp_tree.add_leaf(hash_value, True)
        temp_tree.make_tree()
        verified = temp_tree.validate_proof(proofs, hash_value, root_from_contract)
        return verified

