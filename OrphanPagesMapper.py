#!/usr/bin/env python
import sys

page_id_set = set()
link_id_set = set()
for line in sys.stdin:

	line = line.strip()
	page, links = line.split(': ', 1)
	
	page_id_set.add(page)
	
	links = links.split(' ')
	
	for link in links:
		link_id_set.add(link)

orphans = page_id_set - link_id_set
#not_orphans = page_id_set & link_id_set

for orphan in orphans:		
	sys.stdout.write('o\t%s\n' % (orphan))
	
for not_orphan in link_id_set:
	sys.stdout.write('n\t%s\n' % (not_orphan))
