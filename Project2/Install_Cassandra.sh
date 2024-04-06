# Install python for CQL client
sudo apt-get install python

# Add the Apache repository of Cassandra to the file cassandra.sources.list
echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list

# Add the Apache Cassandra repository keys to the list of trusted keys on the server
curl https://downloads.apache.org/cassandra/KEYS | sudo apt-key add -

# Update the package index from sources:
sudo apt-get update

# Install Cassandra with APT
sudo apt-get install cassandra

# Change the settings of Cassandra
sudo nano /etc/cassandra/cassandra.yaml
# - seeds: address name of all nodes  (A comma separated list of all the IP addresses in your cluster)
# listen_address: address name of current node
# rpc_address: address name of current node

# Start the Cassandra process manually to monitor the service
# This command needed to be executed in all participated nodes
sudo cassandra -Rf

# Open another terminal to query the database
# Check cluster status
nodetool status

# Start the CQL client
# For example: cqlsh cc-miniprojects-1
cqlsh <address-name>

# Stop the Cassandra service:
sudo service cassandra stop
# clear the data
sudo rm -rf /var/lib/cassandra/*