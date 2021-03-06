#!/usr/bin/env python
import sys, operator

current_word = None
current_count = 0
value_list = list()

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
			value_list.append([current_word, current_count])
		current_count = count
		current_word = word
		
if current_word == word:
	value_list.append([current_word, current_count])
	
value_list = sorted(value_list, key=operator.itemgetter(1,0))

for item in sorted(value_list[-10:], key=operator.itemgetter(0)):
	sys.stdout.write('%s\t%s\n' % (item[0], item[1]))
