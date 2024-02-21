#!/usr/bin/env python3
import sys
total = 0 
method = None
for line in sys.stdin:
    method,count = line.strip().split("\t")
    total += int(count)
print(f"{method}\t{total}")
