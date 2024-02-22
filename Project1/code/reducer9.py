#!/usr/bin/env python3
import sys

current_ip,ip = None,None
total_size = 0

for line in sys.stdin:
    ip,size = line.strip().split("\t",1)

    try:
        size = int(size)
    except ValueError:
        size = 0
        continue
    
    if current_ip == ip:
        total_size += size
    else:
        if current_ip:
            print(f"{current_ip}\t{total_size}")
        total_size = size
        current_ip = ip

if current_ip == ip:
    print(f"{current_ip}\t{total_size}")

