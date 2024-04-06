#!/usr/bin/env python3

from cassandra.cluster import Cluster
from datetime import datetime

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('resized_log_keyspace')

with open('resized_log', 'r') as f:
    for line in f:
        parts = line.split(' ')
        ip_address = parts[0]
        date_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
        request_method = parts[5][1:]
        requested_url = parts[6]
        http_version = parts[7][:-1]
        status_code = int(parts[8])
        try:
            response_size = int(parts[9])
        except:
            response_size = None
        user_agent = ' '.join(parts[11:]).strip()[1:-2]

        query = """
            INSERT INTO log_table (ip_address, date_time, request_method, requested_url, http_version, status_code, response_size, user_agent)"
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        #print(query)
        print(ip_address, date_time, request_method, requested_url, http_version, status_code, response_size, user_agent)

        session.execute(query, (ip_address, date_time, request_method, requested_url, http_version, status_code, response_size, user_agent))

cluster.shutdown()