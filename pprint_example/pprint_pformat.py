#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName :    pprint_pformat.py
#  Author :      linuxme@
#  Project :     monitor_maintain
#  Date :        2013-09-01 09:57
#  Description : 
# -----------------------------------------------------

import logging
from pprint import pformat
from pprint_data import data

logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s', )

logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())

