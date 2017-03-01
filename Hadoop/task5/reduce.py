#!/usr/bin/env python
import sys
current_key = None
current_count = 0
key = None
check={}
for line in sys.stdin:
    key, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if current_key == key:
        current_count += count
    else:
        if current_key:
            check[current_key]=current_count 
        current_count = count
        current_key = key

if current_key == key:
    check[current_key]=current_count
maximum=max(check.iterkeys(), key=(lambda key: check[key]))
print '%s\t%s' % (maximum,check[maximum])

