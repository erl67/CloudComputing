#!/usr/bin/env python3
import sys

current_path, path = None, None
total_count = 0

for line in sys.stdin:
    path,count = line.strip().split("\t")
    count = int(count)
    
    if current_path == path:
        total_count += count
    else:
        if current_path:
            print(f"{current_path}\t{total_count}")
        total_count = count
        current_path = path

if current_path == path:
    print(f"{current_path}\t{total_count}")

