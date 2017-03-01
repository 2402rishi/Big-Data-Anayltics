#!/usr/bin/env python
import sys
current_key = None
key = None
weekend_count=0
weekday_count=0
for line in sys.stdin:
    line=line.strip()
    key, day = line.split('\t')
    if current_key == key:
        if str(day) == 'D':
            weekday_count=weekday_count+1
        elif str(day) =='W':
            weekend_count=weekend_count+1
        else:
            continue
    else:
        if current_key:
            print '%s\t%.2f,%.2f' % (current_key,(weekend_count/float(8)),(weekday_count/float(23))) 
        current_key = key
        weekday_count=0
        weekend_count=0
        if str(day) == 'D':
            weekday_count=1
        if str(day)=='W':
            weekend_count=1
        else :
            continue
if current_key == key:
    print '%s\t%.2f,%.2f' % (current_key,(weekend_count/float(8)),(weekday_count/float(23))) 
