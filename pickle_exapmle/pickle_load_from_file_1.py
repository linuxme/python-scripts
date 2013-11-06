#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pickle_load_from_file_1.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 21:29
#  Description : 
# -----------------------------------------------------

try:
    import cPickle as pickle
except:
    import pickle

import pprint
from StringIO import StringIO
from pickle_dump_to_file_1 import SimpleObject
import sys

filename = sys.argv[1]

with open(filename, 'rb') as in_s:
    #Read the data
    while True:
       try:
           o = pickle.load(in_s)
       except:
           break
       else:
           print 'READ: %s (%s)' % (o.name, o.name_backwards)

