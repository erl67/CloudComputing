#!/usr/bin/env python

import sys

# IP identity username timestamp request status size
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

for line in sys.stdin:
    
    # ip, identity, username, timestamp, request, status, size = line.strip().split(None, 6)
    # method, path, _ = request.split(" ", 2)

    # fields = request.strip().split()

    # Extract the request path from the log entry
    # request_path = fields[6]

    # Check if the request path starts with the specified directory

    request_dir = "/images/smilies/"

    if request_dir in line:
        # Emit the request path as the key and 1 as the value
        print(f"{request_dir}\t{1}")