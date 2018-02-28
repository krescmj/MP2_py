#!/usr/bin/env python

import sys
import string
import re
import collections

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopwords = list()
with open(stopWordsPath) as f:
	for line in f.readlines():
		stopwords.append(line.strip())

delimiters = list()
with open(delimitersPath) as f:
	for line in f.readlines():
		for chr in line.strip():
			delimiters.append(chr)

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

regexPattern = '|'.join(map(re.escape, delimiters))

all_words = list()

for line in sys.stdin:
	line = line.strip()
	words = filter(None, re.split(regexPattern, line))
	all_words = all_words + removeStopwords( [x.lower() for x in words], stopwords)

#counts = collections.Counter(all_words).most_common()
	
#for item in counts:
#	sys.stdout.write('%s\t%s\n' % (item[0], item[1]))
for item in all_words:
	sys.stdout.write('%s\t%s\n' % (item, all_words[item]))

