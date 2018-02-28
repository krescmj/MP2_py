#!/usr/bin/env python
import sys

orphan_set = dict()
norphan_set = set()

for line in sys.stdin:
	line = line.strip()
	
	marker, page = line.split(':',1)
	
	if marker == 'o':
		orphan_set.add(page)
	else:
		norphan_set.add(page)
		
orphans = orphan_set - norphan_set

for orphan in orphans:		
	sys.stdout.write('%s\n' % (orphan))