#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
current_count = 0

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)
	
	if current_word == word:
        current_count += count
    else:
        if current_word:
            sys.stdout.write('%s\t%s\n' % (current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    sys.stdout.write('%s\t%s\n' % (current_word, current_count))