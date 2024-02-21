#!/usr/bin/env python3
import sys
total = 0 
ip_addr = ''
for line in sys.stdin:
    ip_addr,count = line.strip().split("\t")
    total += int(count)
print(f"{ip_addr}\t{total}")
