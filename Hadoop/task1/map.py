#!/usr/bin/env python
import os
import csv
import sys
for line in sys.stdin:
    line=line.strip()
    entry = csv.reader([line])
    for row in entry:
        if len(row) ==22 :
            print '%s\t%s, %s' % (row[0],line,'P')
        else :
            print '%s\t%s, %s' % (row[0],line,'O')