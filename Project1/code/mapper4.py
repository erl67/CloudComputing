#!/usr/bin/env python3
import sys

for line in sys.stdin:
    #split out the request line then split again to get the path
    parts = line.strip().split('"')
    if len(parts) >= 2:
        request = parts[1]
        data = request.strip().split()
        if len(data) >= 2:
            path = data[1]
            print(f"{path}\t{1}")

