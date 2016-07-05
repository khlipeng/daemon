#!/usr/bin/python
# -*- coding: utf-8 -*- 

import time
import sys
import os
import subprocess

RUN = 'work.run'

# 重启进程
def restart_program():
    python = sys.executable
    setRunPID(os.getpid())
    os.execl(python, python, * sys.argv)

# 写进程 PID 至运行文件
def setRunPID(pid):
	f = open(RUN, 'w')
	f.write(str(pid))
	f.close()
	return True

# 获取进程
def getRunPID():
	return open(RUN,'r').read()


# 开始任务
def start():
	# 判断任务是否存在
	if os.path.exists(RUN):

		oldPid = getRunPID()
		runpid = str(os.getpid())
		print(oldPid)
		print(runpid)
		if oldPid != runpid :
			restart_program()
		
	setRunPID(os.getpid())
	num = 1
	while(True):
		print(num)
		num += 1
		time.sleep(5)


def stop():
    pid = open(RUN).readline()
    if pid:
    	if subprocess.call(["kill " + pid], shell=True) == 0:
    		print " | ".join(["Stop OK", "PID:%s" % pid])
    		if subprocess.call(["rm " + RUN], shell=True) != 0:
    			print "Delete Permission Denied"
    else:
		print "Stop Error"

def restart():
	print "Restart...."
    

if __name__ == '__main__':
    try:
		arg = sys.argv[1]
    except Exception:
    	print " start | stop | restart "
        arg = ''
    if(arg == 'start'):
    	print "Start..."
        start()
    if(arg == 'stop'):
    	if not os.path.exists(RUN):
    		print "Task does not start"
    		sys.exit(0)
    		
    	print "Stopping..."
        stop()
    if(arg == 'restart'):
    	if not os.path.exists(RUN):
    		print "Task does not start"
    		sys.exit(0)

    	print "Restart..."
        stop()
        time.sleep(1)
        start()
