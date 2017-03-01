#!/usr/bin/env python
import sys
import csv
for line in sys.stdin:
	entry = csv.reader([line])
	for row in entry:
                if len(row)!=22:
		    print '%s\t%s' % (row[2],row[12])
	
