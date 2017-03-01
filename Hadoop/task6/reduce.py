#!/usr/bin/env python
import sys
import heapq
current_key = None
current_count = 0
key = None
check={}
for line in sys.stdin:
    key, count = line.split('\t', 1)
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
k_keys_sorted_by_values = heapq.nlargest(20, check, key=check.get)
for item in k_keys_sorted_by_values:
	print "%s\t%s" % (item,check[item])
