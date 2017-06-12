#!/usr/bin/python
#coding:utf-8

import time
import psutil
import urllib2
import random

while True:
	data = psutil.cpu_times()
        data_m = psutil.virtual_memory()
        data_dp = psutil.disk_partitions()
################################################
        i = random.randint(0,2)
        dpi = data_dp[i]
        dioc = psutil.disk_io_counters()
################################################
        m = psutil.pids()
        n = random.choice(m)
        p = psutil.Process(n)
        psname = p.name()
        pscwd = p.cwd()
        pst = p.status()
        ptime = p.create_time()
        

	dataDict = {
		"userTime":str(data.user),
		"systemTime":str(data.system),
		"waitIo":str(data.iowait),
		"idle":str(data.idle),
                "total":str(data_m.total),
                "used":str(data_m.used),
                "free":str(data_m.free),
                "buffers":str(data_m.buffers),
                "cached":str(data_m.cached),
                "device":str(dpi.device),
                "mountpoint":str(dpi.mountpoint),
                "fstype":str(dpi.fstype),
                "opts":str(dpi.opts),
                "read_ct":str(dioc.read_count),
                "read_bt":str(dioc.read_bytes),
                "read_t":str(dioc.read_time),
                "ps_name":str(psname),
                "ps_cwd":str(pscwd),
                "ps_time":str(pst),
                "ptime":str(ptime)
				}

	strData = "?%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s&%s=%s"
	urlData = strData%("userTime",data.user,"systemTime",data.system,"waitIo",data.iowait,"idle",data.idle,"total",data_m.total,"used",data_m.used,"free",data_m.free,"buffers",data_m.buffers,"cached",data_m.cached,"device",dpi.device,"mountpoint",dpi.mountpoint,"fstype",dpi.fstype,"opts",dpi.opts,"read_ct",dioc.read_count,"read_bt",dioc.read_bytes,"read_t",dioc.read_time,"ps_name",psname,"ps_cwd",pscwd,"ps_time",pst,"ptime",ptime)

	url = "http://192.168.100.116:8000/cgi-bin/index.py"+urlData
	print urllib2.urlopen(url).read()
	
	time.sleep(3)
