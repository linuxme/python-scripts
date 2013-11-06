#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pickle_dump_to_file_1.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 18:17
#  Description : 
# -----------------------------------------------------

try:
    import cPickle as pickle
except:
    import pickle
import sys
import pprint

class SimpleObject(object):
    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('Cpickle'))
    data.append(SimpleObject('last'))

    filename = sys.argv[1]
    with open(filename, 'wb') as out_s:
        #write to the stream
        for o in data:
            print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
            pickle.dump(o, out_s)
