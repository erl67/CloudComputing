#!/usr/bin/env python3
import sys

current_method, method = None, None
total_count = 0

for line in sys.stdin:
    method,count = line.strip().split("\t")
    count = int(count)
    
    if current_method == method:
        total_count += count
    else:
        if current_method:
            print(f"{current_method}\t{total_count}")
        total_count = count
        current_method = method

if current_method == method:
    print(f"{current_method}\t{total_count}")

