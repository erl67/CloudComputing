#!/usr/bin/env python

import sys

path_count = 0

for line in sys.stdin:
    path, count = line.strip().split("\t")
    path_count += int(count)

# output the count for the last path
print(f"{path}\t{path_count}")
