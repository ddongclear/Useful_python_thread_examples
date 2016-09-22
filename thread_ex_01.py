

import thread 
import time 

def print_time(threadName,delay):
	cnt = 0 
	while cnt <100:
		time.sleep(delay)
		cnt += 1 
		print "%s : %s" % (threadName,time.ctime(time.time()))


try:
	thread.start_new_thread(print_time, ("Thread -1 ",2,))
	thread.start_new_thread(print_time, ("Thread -2",1,))

except:
	print "There is something wrong . . . . ."
while 1:
	pass
