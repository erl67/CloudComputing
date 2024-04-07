#!/usr/bin/env python3

from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
#session = cluster.connect('resized_log_keyspace')
#session = cluster.connect('log_keyspace')
#session = cluster.connect('log_keyspace2')
session = cluster.connect('log_keyspace3')

q0 = "SELECT COUNT(*) FROM log_table LIMIT 10"
q0a = "SELECT COUNT(*) FROM log_table"

q1 = "SELECT COUNT(*) FROM log_table WHERE requested_url = '/administrator/index.php' ALLOW FILTERING"
q2 = "SELECT COUNT(*) FROM log_table WHERE ip_address = '96.32.128.5'"

q3 = "SELECT requested_url, COUNT(1) FROM log_table"
#q3 = "SELECT id, requested_url, COUNT(*) FROM log_table GROUP BY requested_url LIMIT 1;"

q4 = "SELECT ip_address, COUNT(*) FROM log_table GROUP BY ip_address"

q5 = "SELECT COUNT(*) FROM log_table WHERE user_agent LIKE '%Mozilla%'"
q6 = "SELECT (COUNT(CASE WHEN request_method = 'GET' THEN 1 END) * 1.0) / COUNT(*) AS ratio FROM log_table WHERE date_time >= '2022-04-02 00:00:00' AND date_time < '2022-04-03 00:00:00'"

q7 = "SELECT COUNT(*) FROM log_table WHERE response_size <= 404 ALLOW FILTERING"
q8 = "SELECT ip_address, COUNT(*) FROM log_table WHERE status_code = 404 GROUP BY ip_address"

queries = [q3]
#queries = [q0, q0a, q1, q2, q3, q4, q5]

for query in queries:
    print(f"\n{query}")

    result = session.execute(query, timeout=600)

    for row in result:
        print(row)
        #count = row[0]
        #print(f"{query=}\n{count=}")



session.shutdown()
cluster.shutdown()