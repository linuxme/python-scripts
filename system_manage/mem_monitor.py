#!/usr/bin/python

##the script for cacti and nagios monitor progress mem usage.
##usage: python mem_monitor.py cacti|nagios progress_name

import sys
import os
import redis
import memcache
import subprocess

script_name = sys.argv[0]
monitor_class = sys.argv[1]
progress_name = sys.argv[2]
get_progress_pid_com = 'ps -ef| grep %s|grep -v "%s"| grep -v grep|awk \'{print $2}\'|xargs' % (progress_name, script_name)
get_total_mem = "cat /proc/meminfo | grep 'MemTotal'| awk -F' ' '{print $2}'"

def cacti_nagios(proname, usedMem,usedRate):
    try:
        if monitor_class == "cacti":
            print "mem_usage:%d"%(usedMem*1000)
        elif monitor_class == "nagios":
            if usedRate >= 80:
                print "%s used mem exceed " % proname + "80%, please check.."
                sys.exit(2)
            else:
                print "%s use mem is %d " % (proname, usedRate) +"%"
                sys.exit(0)
        else:
                print "print input python \033[1;31;40m%s\033[0m cacti|nagios progress_name" % script_name
    except:
        pass

def get_progress_mem():
    """get progress mem"""
    try:
        sum_mem = 0

        progress_pid = os.popen(get_progress_pid_com).readlines()
        for i in progress_pid:
            pass
        item = i.strip('\n').split(' ')

        for k in item:
            get_progress_mem = "cat /proc/%s/status|grep VmRSS|awk '{print $2}'" % k.strip()
            mem = os.popen(get_progress_mem).readlines()
            for j in mem:
                pass
            use_mem = j.strip('\n ')
            use_mem = int(use_mem)
            sum_mem += use_mem
        total_mem = os.popen(get_total_mem).readlines()
        for m in total_mem:
            pass
        total_mem = m.strip('\n ')
        total_mem = float(total_mem) 
        mem_usage_rate = sum_mem / total_mem * 100 
        cacti_nagios(progress_name, sum_mem, mem_usage_rate)
    except:
        print "please check the \033[1;31;40m%s\033[0m progess name is Correct Spelling ?" % progress_name
        sys.exit(2)
       

def get_redis_mem():
    try:
        con = redis.Redis(host = 'localhost', port = 6379) 
        if con.ping() == True:
            max_mem = con.config_get(pattern='maxmemory').get('maxmemory')
            used_mem = con.info().get('used_memory')
            used_rate = float(used_mem) / float(max_mem) * 100

            cacti_nagios(progress_name, used_mem, used_rate)
        else:
           print "Cannot connect the redis"
           sys.exit(2)
    except Exception as e:
       print e.message


def get_memcache_mem():
    try:
        exec_com = "echo 'stats'|nc localhost 11211" 
        result = os.popen(exec_com).readlines()
        max_conf_set = float(result[-10].strip('\n').split(' ')[2])
        used_mem = float(result[-5].strip('\n').split(' ')[2])/1000
        used_rate = used_mem / max_conf_set * 100
        
        cacti_nagios(progress_name, used_mem, used_rate)
    except Exception as e:
        print e.message

if progress_name == "redis":
    get_redis_mem()
elif progress_name == "memached" or progress_name == "memcache":
    get_memcache_mem()
else:
    get_progress_mem() 
