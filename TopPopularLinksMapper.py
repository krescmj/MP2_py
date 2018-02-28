#!/usr/bin/env python
import sys, operator

value_list = list()

for line in sys.stdin:

	line = line.strip()
	link, count = line.split('\t', 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
		
	value_list.append([link, count])
	
value_list = sorted(value_list, key=operator.itemgetter(1,0))

for item in value_list[-10:]:
	sys.stdout.write('%s\t%s\n' % (item[0], item[1]))
