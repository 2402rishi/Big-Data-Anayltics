#!/usr/bin/env python
import sys
current_key = None
current_count = 0
key = None
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
            print '%s\t%s' % (current_key, current_count)
        current_count = count
        current_key = key

# do not forget to output the last word if needed!
if current_key == key:
    print '%s\t%s' % (current_key, current_count)

