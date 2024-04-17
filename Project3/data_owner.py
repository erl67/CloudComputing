from db_provider import Server
import merkletools
class DataOwner:
    #init data owner with the key value data
    #specify the server object
    def __init__(self,key_value_data,server,blockchain):
        self.data= key_value_data
        self.server= server
        self.merkle_tree = None
        self.blockchain = blockchain

    #insert data to self.server
    def insert_data_to_server(self):
        pass

    # build merkle tree on data owner side to get the merkle root, key+value as values
    # You can use functions provided by merkletools
    def build_merkle_tree(self):
        pass

    # upload self.merkle_tree to self.server
    def upload_merkle_tree_to_server(self):
        pass


    # get merkle root from self.merkle_tree
    def get_merkle_root(self):
        pass

    #upload merkle root to self.blockchains
    def upload_merkle_root_to_blockchain(self):
        pass






