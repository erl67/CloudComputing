#!/usr/bin/env python3
import sys

date_check = "16/Jan/2022"
status_code = 200

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
            status = parts[2].split()
            code,size = int(status[0]), int(status[1])
            if code == status_code:
                #print(code,size)
                print(f"{date}\t{size}")

