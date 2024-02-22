#!/usr/bin/env python3
import sys

date_check,total = '16/Jan/2022', 0

for line in sys.stdin:
    date,size = line.strip().split("\t")
    size = int(size)
    if date == date_check:
        total += size
print(f"{date_check}\t{total}")

