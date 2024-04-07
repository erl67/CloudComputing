
Part 1:

These were the commands used to create the cassandra installation and are shown in the left half
of the screenshot. I had to download it directly because the repositories didn't work.

PS C:\Users\x5769> ssh -i .ssh/key_group15 root@155.98.37.38
PS C:\Users\x5769> scp -i .ssh/key_group15 .ssh/key_group15 root@155.98.37.38:/root/.ssh
PS C:\Users\x5769> scp -i .ssh/key_group15 C:/resized_log root@155.98.37.38:/
root@vm-1:~# curl -OL https://dlcdn.apache.org/cassandra/4.1.4/apache-cassandra-4.1.4-bin.tar.gz
root@vm-1:~# tar xzvf apache-cassandra-4.1.4-bin.tar.gz
cd /root/apache-cassandra-4.1.4
nano /root/apache-cassandra-4.1.4/conf/cassandra.yaml
./bin/cassandra
./bin/nodetool status
./import_log.py


Part 2:
For this part I used the python cassandra driver. I wrote the program import_log.py that 
read, modified, and inserted the log files to cassandra. This took very many tries as the 
table had very unusual characteristics. It was much different than SQL and none of the 
queries worked the way I wanted them to, which required constant trial and error. 
Also it required constant shutting down of cassandra to edit the cassandra.yaml file.


apt install python3-pip
pip install cassandra-driver
./cqlsh
describe resized_log_keyspace.log_table;
truncate resized_log_keyspace.log_table;
cqlsh --request-timeout=600
cqlsh> select count(*) from resized_log_keyspace.log_table;

cqlsh> CREATE KEYSPACE IF NOT EXISTS log_keyspace2 WITH replication = {'class':'SimpleStrategy','replication_factor':1};
cqlsh> CREATE TABLE IF NOT EXISTS log_keyspace2.log_table (
id INT PRIMARY KEY, ip_address TEXT, date_time TIMESTAMP, request_method TEXT,
requested_url TEXT, http_version TEXT, status_code INT, response_size INT, user_agent TEXT);


cqlsh> select count(*) from log_keyspace2.log_table;
SELECT * FROM log_keyspace2.log_table LIMIT 10;
CREATE KEYSPACE IF NOT EXISTS log_keyspace3 WITH replication = {'class':'SimpleStrategy','replication_factor':1};
CREATE TABLE log_keyspace3.log_table (
  id int,
  date_time timestamp,
  http_version text,
  ip_address text,
  request_method text,
  requested_url text,
  response_size int,
  status_code int,
  user_agent text,
  PRIMARY KEY ((ip_address), requested_url, id)
) WITH CLUSTERING ORDER BY (requested_url ASC, id DESC);

CREATE TABLE log_keyspace3.log_table (
  id int,
  date_time timestamp,
  http_version text,
  ip_address text,
  request_method text,
  requested_url text,
  response_size int,
  status_code int,
  user_agent text,
  PRIMARY KEY ((requested_url), ip_address, id)
) WITH CLUSTERING ORDER BY (ip_address ASC, id DESC);


CREATE INDEX idx_user_agent ON log_keyspace2.log_table (user_agent);

CREATE CUSTOM INDEX idx_user_agent_sasi ON log_keyspace3.log_table (user_agent) 
USING 'org.apache.cassandra.index.sasi.SASIIndex'
WITH OPTIONS = { 
  'analyzer_class': 'org.apache.cassandra.index.sasi.analyzer.NonTokenizingAnalyzer',
  'case_sensitive': 'false'
};


Part 3:
For the queries, I tested them in cqlsh and then I put them all in a python file, because
the cqlsh often came back with weird errors. Doing it in python was much more familiar because
I've used it a lot with SQL, and it allowed me to fix the results of certain queries that cqlsh didn't allow.
Also running queries in python was more reliable in terms of timeouts.

The python file can be run with ./query.py
I put the results in results.txt. I also included the console output for parts 1 and 2.




Sources:
https://cassandra.apache.org/doc/stable/cassandra/getting_started/installing.html
https://cassandra.apache.org/doc/stable/cassandra/getting_started/configuring.html
https://cassandra.apache.org/doc/stable/cassandra/cql/dml.html#select
https://docs.datastax.com/en/dse/6.7/cql/cql/cql_using/useSASIIndex.html