#!/usr/bin/env python
import sys, operator

orphan_set = set()
norphan_set = set()

for line in sys.stdin:
	line = line.strip()
	
	marker, page = line.split('\t',1)
	
	if marker == 'o':
#		if page not in norphan_set:
		orphan_set.add(page)
	elif marker == 'n':
		#if page in orphan_set:
		#	orphan_set.remove(page)
		norphan_set.add(page)

orphans = orphan_set - norphan_set
orphans = sorted(orphan_set)

for orphan in orphans:		
	sys.stdout.write('%s\n' % (orphan))
