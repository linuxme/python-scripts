#!/bin/bash
from __future__ import division
import sys

read_file=sys.argv[1]
sum_value = {}
count = {}
max_value = {}
min_value = {}


for line in open(read_file):
    line_data = line.split(' ')
    try:
        if '?' in line_data[18]:
            line_data[18] = line_data[18].split('?')[0]
        if int(line_data[24]) > int(sys.argv[2]):
            if not sum_value.has_key(line_data[18]):
                sum_value[line_data[18]] = int(line_data[24])
                max_value[line_data[18]] = sum_value[line_data[18]]
                min_value[line_data[18]] = sum_value[line_data[18]]
                count[line_data[18]] = 1
            else:
                if max_value[line_data[18]] <= int(line_data[24]):
                    max_value[line_data[18]] = int(line_data[24])
                if min_value[line_data[18]] >= int(line_data[24]):
                    min_value[line_data[18]] = int(line_data[24])
                sum_value[line_data[18]] += int(line_data[24]) 
                count[line_data[18]] += 1
    except:
        pass
    
for (key, value) in sum_value.items():
    print "%-25s  %-5d %-10.2f %-5d %d" % (key,count[key],sum_value[key]/count[key],max_value[key],min_value[key])
