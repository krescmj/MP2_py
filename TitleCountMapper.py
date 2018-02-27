#!/usr/bin/env python

import sys
import string
import re
import collections

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

regexPattern = '|'.join(map(re.escape, open(delimitersPath).readlines()))

all_words = list()

for line in sys.stdin:
	line = line.strip()
	words = re.split(regexPattern, line)
	all_words = all_words + (removeStopwords( [x.lower() for x in words], open(stopWordsPath).readlines()))
	
counts = collections.Counter(all_words).most_common()
	
for item in counts:
	sys.stdout.write('%s\t%s\n' % (item[0], item[1]))

