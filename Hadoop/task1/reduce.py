#!/usr/bin/env python
import sys
import csv
previous_key = None
key = None
previous_file=None
previous_record=None
for line in sys.stdin:
    line=line.strip()
    key, record = line.split('\t')
    key=key.strip()
    abc=record.split(',')
    file=abc[len(abc)-1]
    file=file.strip()
    record=record[:len(record)-1]
    record=record.strip()
    if previous_key == key:
        previous_key=None
        previous_record=None
        previous_file=None
        continue
    else:
        if previous_key is not None and previous_file == 'P':
            entry = csv.reader([previous_record])
            for row in entry :
                print '%s\t%s, %s, %s, %s' % (previous_key,row[14],row[6],row[2],row[1])
        previous_key=key
        previous_file=file
        previous_record=record
if previous_key is not None and previous_file == 'P':
    entry = csv.reader([previous_record])
    for row in entry :
        print '%s\t%s, %s, %s, %s' % (previous_key,row[14],row[6],row[2],row[1])

        