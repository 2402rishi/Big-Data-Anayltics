#!/usr/bin/env python
import os
import csv
import sys
weekends=[5, 6, 12, 13, 19, 20, 26, 27]
for line in sys.stdin:
    entry = csv.reader([line])
    for row in entry:
        if len(row) == 22 :
            date= int(row[1][-2:])
            if date in weekends:
                print '%s\t%s' % (row[2],'W')
            else :
                print '%s\t%s' % (row[2],'D')
