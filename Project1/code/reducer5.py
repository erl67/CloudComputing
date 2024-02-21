#!/usr/bin/env python3
import sys

current_ip, ip = None, None
total_count = 0

for line in sys.stdin:
    ip,count = line.strip().split("\t")
    count = int(count)
    
    if current_ip == ip:
        total_count += count
    else:
        if current_ip:
            print(f"{current_ip}\t{total_count}")
        total_count = count
        current_ip = ip

if current_ip == ip:
    print(f"{current_ip}\t{total_count}")

