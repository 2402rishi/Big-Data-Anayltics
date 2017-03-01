#!/usr/bin/env python
import os
import csv
import sys
for line in sys.stdin:
    line=line.strip()
    entry = csv.reader([line])
    for row in entry:
        if len(row) == 22 :
	    if row[16] !='NY':
	        print '%s\t%s' % ("Other",1)
	    else:
	        print '%s\t%s' % (row[16],1)

