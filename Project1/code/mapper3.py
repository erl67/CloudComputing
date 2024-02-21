#!/usr/bin/env python3
import sys

for line in sys.stdin:
    #split out the request line
    parts = line.strip().split('"')
    if len(parts) >= 2:
        request = parts[1]
        data = request.strip().split()
        if len(data) >= 2:
            method = data[0]
            print(f"{method}\t{1}")

