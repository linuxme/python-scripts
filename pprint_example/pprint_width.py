#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pprint_width.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 10:28
#  Description : 
# -----------------------------------------------------

from pprint import pprint
from pprint_data import data

for width in [ 80, 5, 1 ]:
    print 'WIDTH =', width
    pprint(data, width=width)
    print

