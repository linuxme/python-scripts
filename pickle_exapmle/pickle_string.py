#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pickle_string.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 10:32
#  Description : 
# -----------------------------------------------------

try:
    import cpickle as pickle
except:
    import pickle
import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'DATA:',
pprint.pprint(data)
data_string = pickle.dumps(data)
print 'PICKLE: %r' % data_string
print 'PICKLE: %s' % data_string

