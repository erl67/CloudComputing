#!/usr/bin/env python3
# this doesn't work, although it seemed to at first ?
import sys
from mrjob.job import MRJob

text = "Hello World Hellow World"

n = 2
ngrams = []

print(n)

class MRNgram(MRJob):

    def mapper(self, _, line):
        #print(line)
        
        for line in sys.stdin:
            words = line.strip().split()
#            print(words)
                   
            for word in words:
                ngram = [word[i:i+n] for i in range(len(word)-n+1)]
                #ngrams.extend(ngram)
#                for gram in ngram:
#                    yield gram, 1

        for ngram in ngrams:
            yield (ngram, 1)


    def reducer(self, ngram, counts):
        #print(ngram, sum(counts))
        yield (ngram, sum(counts))



if __name__ == '__main__':
    MRNgram.run()

