#!/usr/bin/env python
import sys

for line in sys.stdin:
	
	line = line.strip()
	word, count = line.split('\t', 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
	
	sys.stdout.write('%s\n' % (count))
