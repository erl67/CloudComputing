from cassandra.cluster import Cluster
import hashlib
import json

class Server:
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.merkle_tree = None
        self.keyspace = "project3"  # keyspace(database) name for storing data
        self.table = "data"  # table name for storing data

        # Create keyspace and corresponding table
        self.session.execute("CREATE KEYSPACE IF NOT EXISTS " + self.keyspace + " WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};")
        self.session.set_keyspace(self.keyspace)
        self.session.execute(f"CREATE TABLE IF NOT EXISTS {self.table} (key text PRIMARY KEY, value text);")

    # Use insert syntax to add new key value pair to the target table
    def add_data(self, key, value):
        query = "INSERT INTO data (key, value) VALUES (%s, %s)"
        self.session.execute(query, (key, value))

    # Retrieve value by key
    def get_data(self, key):
        query = f"SELECT value FROM {self.table} WHERE key='{key}';"
        result = self.session.execute(query)
        return result.one().value if result.one() else None

    def get_merkle_tree(self):
        return self.merkle_tree

    def set_merkle_tree(self, merkle_tree):
        self.merkle_tree = merkle_tree

    def get_merkle_proof(self, key):
        if self.merkle_tree:
            value = self.get_data(key)
            if value:
                proof = self.merkle_tree.get_proof(key + value)
                return proof
        return None

