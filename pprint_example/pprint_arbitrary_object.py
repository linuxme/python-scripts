#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pprint_arbitrary_object.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 10:09
#  Description : 
# -----------------------------------------------------

from pprint import pprint

class node(object):
    def __init__(self, name,contents=[]):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return ( 'node(' + repr(self.name) + ',' + repr(self.contents) +')' )

trees = [ node('node-1'),
        node('node-2', [ node('node-2-1')]), 
        node('node-3', [ node('node-2-1')]), 
        ]

pprint(trees)
