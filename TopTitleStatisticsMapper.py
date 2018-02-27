#!/usr/bin/env python
import sys

sum = 0
minimum = None
maximum = 0
size = 0

for line in sys.stdin:
	
	line = line.strip()
	word, count = line.split('\t', 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
	
	sum += count
	
	if minimum == None:
		minimum = count
	else:
		minimum = min(minimum,count)
		
	maximum = max(maximum,count)
	size += 1
	
sys.stdout.write('%s\t%s\t%s\t%s\n' % (sum, minimum, maximum, size))
