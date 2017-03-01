#!/usr/bin/env python
import os
import csv
import sys
for line in sys.stdin:
    line=line.strip()
    entry=csv.reader([line])
    for row in entry :
        if len(row) == 22 : 
            print '%s, %s\t%s' % (row[14],row[16],1)


