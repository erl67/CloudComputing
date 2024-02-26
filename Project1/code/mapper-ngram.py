#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    n = 2

#print(n)
for line in sys.stdin:
    ngrams = []
    words = line.strip().split()
    #print(words)
    
    for word in words:
        ngram = [word[i:i+n] for i in range(len(word)-n+1)]
        ngrams.extend(ngram)

    #print(ngrams)

    for ngram in ngrams:
        print(f"{ngram}\t{1}")
