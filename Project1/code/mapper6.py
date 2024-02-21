#!/usr/bin/env python3
import sys

method = "POST"
for line in sys.stdin:
    #split out the request line
    parts = line.strip().split('"')
    if len(parts) >= 2:
        request = parts[1]
        data = request.strip().split()
        if len(data) >= 2 and data[0].startswith(method):
            print(f"{method}\t{1}")

