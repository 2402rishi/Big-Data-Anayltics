#!/usr/bin/env python
import sys
current_license_type = None
current_amount = 0
count=1
license_type = None
for line in sys.stdin:
    try:
        license_type, amount = line.split('\t')
        amount = float(amount)
    except :
        continue
    if current_license_type == license_type:
        current_amount += amount
        count=count+1
    else:
        if current_license_type:            
            print '%s\t%.2f, %.2f' % (current_license_type,current_amount,current_amount/count)
        current_license_type= license_type
        current_amount = amount
        count=1

if current_license_type == license_type:
    print '%s\t%.2f, %.2f' % (current_license_type,current_amount,current_amount/count)


