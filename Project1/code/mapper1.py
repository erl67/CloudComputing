#!/usr/bin/env python3
import sys
request_dir="/images/smilies"
for line in sys.stdin:
    if request_dir in line:
        print(f"{request_dir}\t{1}")
