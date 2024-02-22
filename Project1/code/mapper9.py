#!/usr/bin/env python3
import sys

#top 3 IPs from problem 5 
top3 = ['47.39.156.135', '96.32.128.5', '73.169.232.206']

for line in sys.stdin:
    #split out the ip address
    parts = line.strip().split('"')
    if len(parts) >= 2:
        ip_address = parts[0].split()[0]
        if ip_address in top3:
            #get the data size transferred
            size = int(parts[2].split()[1])
            #if size > 0 and len(ip_address) > 8:
            print(f"{ip_address}\t{size}")

