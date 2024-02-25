#!/usr/bin/env python3
import sys

current_ngram, ngram = None, None
total_count = 0

for line in sys.stdin:
    #print(line)   
    ngram, count = line.strip().split("\t")
    count = int(count) 
    
    if current_ngram == ngram:
        total_count += count
    else:
        if current_ngram:
            print(f"{current_ngram}\t{total_count}")
        total_count = count
        current_ngram = ngram

if current_ngram == ngram:
    print(f"{current_ngram}\t{total_count}")

