#!/usr/bin/env python3
import sys

code = "404"

for line in sys.stdin:
    parts = line.strip().split('"')
    if len(parts) >= 2:
        status_code = parts[2].split()[0]
        if status_code == code: 
            print(f"{status_code}\t{1}")

