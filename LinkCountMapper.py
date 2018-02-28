#!/usr/bin/env python
import sys, collections

counts = collections.Counter()

for line in sys.stdin:

	line = line.strip()
	page, links = line.split(': ', 1)

	links = links.split(' ')
	
	for link in links:
		if link is not ' ':
			counts.update([link])
		
#print counts.most_common()

for item in counts:
	sys.stdout.write('%s\t%s\n' % (item, counts[item]))
