#!/usr/bin/env python3
import sys
from mrjob.job import MRJob
from mrjob.util import cmd_line 

text = "Hello World Hellow World"

n = 2

#if len(sys.argv) == 2:
#    n = int(sys.argv[1])

#print(n, sys.argv)

#for arg in sys.argv:
#    print(arg)

class MRNgram(MRJob):

    def mapper(self, _, line):

#        n = int(self.options.size)
        n = 2
        print(n)
#        n = x

        for line in sys.stdin:
            try:
                words = line.strip().split()
            except ValueError:
                continue
            #print(words)
    
       
        for word in words:
            ngram = [word[i:i+n] for i in range(len(word)-n+1)]
            for gram in ngram:
                yield(gram, 1)


    def reducer(self, ngram, counts):
        yield(ngram, sum(counts))

#    def config(self):
#        super(MRNgram, self).config()
#        self.add_passthru_arg('--size', type-int, default=2, help="n-gram length")

if __name__ == '__main__':
#    MRNgram.add_passthru_arg('--n', type=int, help='n-gram length')
#    args = sys.argv[1:]
#    print(args)
#    i = args.index('--size') if '--size' in args else -1
#    if i != -1 and i + 1 < len(args):
#        size = int(args[i+1])
#    else:
#        size = 2

#    size = 2
    
    print(sys.argv)
    args = sys.argv[1:]

#    if '--size' in args:
#        i = args.index('--size')
#        if i+ 1 < len(args):
#            size = int(args[i+1])
#        args = args[:i] + args[i+2:]
#    MRNgram.options.size = size
#    MRNgram.run(size)
#    mr_job = MRNgram(args=['--size', str(size)])
    mr_job = MRNgram(args=args)
#    mr_job.options.size = size
    mr_job.run()

