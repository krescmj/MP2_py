#!/usr/bin/env python
from operator import itemgetter
import sys, collections

current_word = None
current_count = 0
word_counts = collections.Counter()

# input comes from STDIN
for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
	
	if current_word == word:
		current_count += count
	else:
		if current_word:
			#sys.stdout.write('%s\t%s\n' % (current_word, current_count))
			word_counts.update([current_word,current_count])
		current_count = count
		current_word = word

if current_word == word:
    #sys.stdout.write('%s\t%s\n' % (current_word, current_count))
	word_counts.update([current_word,current_count])
	
counts = word_counts.most_common()

ret = []

temp = [counts[0][0]]
temp_count = counts[0][1]
for x in range(1, len(counts)):
	if temp_count == counts[x][1]:
		temp.append(counts[x][0])
		temp.sort()
	else:
		if x > 9:
			break
		
		ret = ret + temp
		temp = [counts[x][0]]
		temp_count = counts[x][1]

ret = ret + temp
ret = ret[0:10]

#for word in ret:
for x in range(0, len(ret)):
	word = ret[len(ret)-x]
	sys.stdout.write('%s\t%s\n' % (word, word_counts[word]))