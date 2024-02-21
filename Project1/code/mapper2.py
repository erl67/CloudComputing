#!/usr/bin/env python3
import sys
ip_addr="96.32.128.5"
for line in sys.stdin:
    if line.startswith(ip_addr):
        print(f"{ip_addr}\t{1}")

