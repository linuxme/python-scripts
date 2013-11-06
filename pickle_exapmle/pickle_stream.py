#!/usr/bin/env python
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
from StringIO import StringIO

class SimpleObject(object):
    
    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cpickle'))
data.append(SimpleObject('last'))

#Simulate a file with StringIO
out_s = StringIO()

#Write to the stream
for o in data:
    print 'WRITING : %s (%s)' %(o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()

#Set up a read-able stream
in_s = StringIO(out_s.getvalue())

#Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'READ : %s (%s)' % (o.name, o.name_backwards)
