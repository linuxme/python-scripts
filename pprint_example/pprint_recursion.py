#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pprint_recursion.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 10:21
#  Description : 
# -----------------------------------------------------


from pprint import pprint

local_data = [ 'a', 'b', 1, 2 ]
local_data.append(local_data)

print 'id(local_data) =>', id(local_data)
pprint(local_data)

