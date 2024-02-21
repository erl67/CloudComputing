#!/usr/bin/env python3
import sys

for line in sys.stdin:
    #split out the ip address
    parts = line.strip().split('"')
    if len(parts) >= 2:
        ip_address = parts[0].split()[0]
        print(f"{ip_address}\t{1}")

