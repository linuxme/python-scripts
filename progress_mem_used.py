#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from optparse import OptionParser
import sys, os, commands, string
sum_mem = 0

def get_mem_usage(pid):
    '''
    得到进程的pid号，查看/proc/pid/status文件，格式如下
    VmPeak:    23836 kB
    VmSize:    23796 kB
    VmLck:         0 kB
    VmHWM:      2012 kB
    VmRSS:      2012 kB
    VmData:      680 kB
    VmStk:        88 kB
    VmExe:       116 kB
    VmLib:      2356 kB
    然后将其放到字典中，以：为分隔第一列是key，第二列是value，最后函数返回字典mem
    '''
    mem = {} #init variable as dictionary
    pid_status_path='/proc/%s/status'%pid
    with open(pid_status_path) as f:
        for line in f:
            mem[line.split(':')[0]] = line.split(':')[1].strip()
    return mem

if __name__ == '__main__':
    optparser = OptionParser()
    #optparser.add_option('-l', '--helpp',  dest='mannul', help='mannul')

    options, args = optparser.parse_args()
    if args[0]:
        #get daemon progress pids
        comm="ps aux|grep %s|grep -v 'python %s'|grep -v grep|awk '{print $2}'"% (args[0], sys.argv[0])
    
        #change pids string to pids list
        output = string.split(commands.getoutput(comm))
    
        #get every pid mem_usaged,then add together
        for i in output:
            mem = get_mem_usage(i)
            mem_usage = int(string.split(mem['VmRSS'])[0])
            sum_mem += mem_usage
    
        #print all using mem
        print ('mem_usage:',sum_mem,'KB')
