#!/usr/bin/env python

import sys
import string
import re
import collections

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

# TODO
#with open(stopWordsPath) as f:
#	print input_lines
#.readlines()
    # TODO
def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

#TODO 
#with open(delimitersPath) as f:
regexPattern = '|'.join(map(re.escape, open(delimitersPath).readlines()))
    # TODO

for line in sys.stdin:
	line = removeStopwords( re.split(regexPattern, line).lower(), open(delimitersPath).readlines())
	
	counts = collections.Counter(words).most_common()
	
	#result = dict()
	#for x in range(0, len(counts)):
	#	result.ap
	sys.stdout.write(counts)
	#return counts
	
    # TODO

