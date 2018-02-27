#!/usr/bin/env python
import sys, math

sum = 0
minimum = None
maximum = 0
size = 0
variance = 0

counts = list()
for line in sys.stdin:
	
	count = line.strip()
	
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
	
	counts.append(count) 
	
mean = sum/len(counts)

var_sum = 0
for count in counts:
	var_sum += math.pow(count - mean, 2)
	
variance = var_sum/len(counts)

sys.stdout.write('Mean\t%s\n' % (mean))
sys.stdout.write('Sum\t%s\n' % (sum))
sys.stdout.write('Min\t%s\n' % (minimum))
sys.stdout.write('Max\t%s\n' % (maximum))
sys.stdout.write('Var\t%s\n' % (variance))
