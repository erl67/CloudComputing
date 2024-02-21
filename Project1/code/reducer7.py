#!/usr/bin/env python3
import sys

code,total = '404', 0

for line in sys.stdin:
    status,count = line.strip().split("\t")
    count = int(count)
    if status == code:
        total += count
print(f"{code}\t{total}")

