#!/usr/bin/env python
import sys


leaguePath = sys.argv[1]

league_list = list()
with open(leaguePath) as f:
	for league in f.readlines():
		league_list.append(league.strip())


for line in sys.stdin:

	line = line.strip()
	page, count = line.split('\t', 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
		
	if page in league_list:
		sys.stdout.write('%s\t%s\n' % (page, count))
		league_list.remove(page)

for page in league_list:
	sys.stdout.write('%s\t%s\n' % (page, 0))
