#!/usr/bin/env python3
import sys

date_check = "19/Dec/2020"

for line in sys.stdin:
    parts = line.strip().split('"')
    #print(parts)
    if len(parts) >= 2:
        #extract date
        date = parts[0].split('[', 1)
        date = date[1].split(':',1)[0]
        #print(date)

        if date == date_check:
            #get data size
            #print(True, parts[2])
            size = parts[2].split()[-1]
            #print(size)
            print(f"{date}\t{size}")

