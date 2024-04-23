Setup: 

Use winSCP to upload files to VM

ssh ubuntu@155.98.37.20


echo "colorscheme evening" >> ~/.vimrc

sudo apt-get update
sudo apt get upgrade

apt install python3-pip
pip install cassandra-driver

root@vm-1:~# curl -OL https://dlcdn.apache.org/cassandra/4.1.4/apache-cassandra-4.1.4-bin.tar.gz
root@vm-1:~# tar xzvf apache-cassandra-4.1.4-bin.tar.gz
cd /home/ubuntu/apache-cassandra-4.1.4/bin

sudo apt install openjdk-8-jdk-headless

sudo ./cassandra -Rf

pip3 install multidict yarl aiosignal idna_ssl async-timeout async_timeout Cython
pip3 install web3==5.31.4

Install nvm and ganache as per the setup.sh script


Fix for solidity no-op code, also involved a small change to blockchain.py
python3
>>> from solcx import install_solc
>>> install_solc('0.8.0')



Results:

The screenshot of the setup is shown in setup.png and the screenshot of the results is in results.png
The first execution shows when an attack has not happened, and the second execution shows when and attack has happened.
The screenshot also includes the cassandra table.

The table was verified by the commands:
cqlsh
USE project3;
SELECT * FROM data;
