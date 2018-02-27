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

all_words = list()
#test = "sdafsad,sdafsda"
#for line in test:
for line in sys.stdin:
	line = line.strip()
	words = re.split(regexPattern, line)
	all_words = all_words + (removeStopwords( [x.lower() for x in words], open(stopWordsPath).readlines()))
	
counts = collections.Counter(all_words).most_common()
	
	#result = dict()
	#for x in range(0, len(counts)):
	#	result.ap
	
for item in counts:
	sys.stdout.write('%s\t%s\n' % (item[0], item[1]))
	#return counts
	
    # TODO

