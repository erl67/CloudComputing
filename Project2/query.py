#!/usr/bin/env python3

from cassandra.cluster import Cluster
from collections import defaultdict

cluster = Cluster(['127.0.0.1'])
#session = cluster.connect('resized_log_keyspace')
#session = cluster.connect('log_keyspace')
#session = cluster.connect('log_keyspace2')
session = cluster.connect('log_keyspace3')

q0 = "SELECT * FROM log_table LIMIT 10"
q0a = "SELECT COUNT(*) FROM log_table"
q1 = "SELECT COUNT(*) FROM log_table WHERE requested_url = '/administrator/index.php' ALLOW FILTERING"
q2 = "SELECT COUNT(*) FROM log_table WHERE ip_address = '96.32.128.5'"
q3 = "SELECT requested_url FROM log_table"
#q3 = "SELECT requested_url, COUNT(*) FROM log_table GROUP BY requested_url" #doesn't work after 4 table rebuilds
q4 = "SELECT ip_address, COUNT(*) FROM log_table GROUP BY ip_address"
q5 = "SELECT user_agent FROM log_table"
#q5 = "SELECT COUNT(*) FROM log_table WHERE user_agent LIKE '%Mozilla%'" #can't query even with sasii
q6 = "SELECT request_method FROM log_table WHERE date_time >= '2022-04-02' AND date_time < '2022-04-03' ALLOW FILTERING"
q6b = "SELECT request_method FROM log_table WHERE date_time >= '2022-04-02' AND date_time < '2022-04-03' AND request_method = 'GET' ALLOW FILTERING"
q7 = "SELECT COUNT(*) FROM log_table WHERE response_size <= 404 ALLOW FILTERING"
q8 = "SELECT ip_address, COUNT(*) FROM log_table WHERE status_code = 404 GROUP BY ip_address ALLOW FILTERING"


r1 = session.execute(q1, timeout=600)
print(f"\n{q1} =\n{r1.one()[0]}\n")
r2 = session.execute(q2, timeout=600)
print(f"{q2} =\n{r2.one()[0]}\n")

r3 = session.execute(q3, timeout=600)
url_count = defaultdict(int)
for row in r3:
    url_count[row.requested_url]+=1
most = max(url_count, key=url_count.get)
print(f"{q3} =\n{most} : {url_count[most]}\n")

r4 = session.execute(q4, timeout=600)
r4_sorted = sorted(r4, key=lambda x: x.count, reverse=True)
print(f"{q4} =\n{r4_sorted[0]}\n")

r5 = session.execute(q5, timeout=600)
count = sum(1 for row in r5 if 'Mozilla' in row.user_agent)
print(f"{q5} LIKE %Mozilla% =\n{count}\n")

r6 = session.execute(q6, timeout=600)
r6b = session.execute(q6b, timeout=600)
count6 = len(list(r6))
count6b = len(list(r6b))
print(f"{q6b} / {q6} =\n{count6b/count6:.4%}\n")

r7 = session.execute(q7, timeout=600)
print(f"{q7} =\n{r7.one()[0]}\n")

r8 = session.execute(q8, timeout=600)
r8_filtered = [row for row in r8 if row.count > 10]
r8_sorted = sorted(r8_filtered, key=lambda x: x.count, reverse=True)
r8_dict = {row.ip_address: row.count for row in r8_sorted}
print(f"{q8} =\n{r8_dict}\n")


session.shutdown()
cluster.shutdown()