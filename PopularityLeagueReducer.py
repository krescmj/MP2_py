#!/usr/bin/env python
import sys, operator

page_list = list()

# input comes from STDIN
for line in sys.stdin:

	line = line.strip()
	page, count = line.split('\t', 1)
	
	page_list.append([page, count])
	
page_list = sorted(page_list, key=operator.itemgetter(1,0))
page_list = list(reversed(sorted(page_list[-10:], key=operator.itemgetter(0))))

rank_list = sorted(page_list, key=operator.itemgetter(0,1))

for x in range(0, len(page_list)):
	
	item = page_list[x]
	sys.stdout.write('%s\t%s\n' % (item[0], rank_list.index(item)))