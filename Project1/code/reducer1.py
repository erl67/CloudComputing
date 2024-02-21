#!/usr/bin/env python3
import sys
total = 0 
path = ''
for line in sys.stdin:
    path,count = line.strip().split("\t")
    total += int(count)
print(f"{path}\t{total}")
