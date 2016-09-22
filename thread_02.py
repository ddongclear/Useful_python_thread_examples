import thread
import time 

from Queue import Queue



q = Queue(10)

def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1 
		print "%s : %s" % (threadName , time.ctime(time.time()))
#thread.start_new_thread(print_time,(5,))




try:
	thread.start_new_thread(print_time,("Thread -1 ",2,))
	thread.start_new_thread(print_time,("Thread -2",4))
except:
	print "Error unable to start thread"



q.get()

if __name__ == '__main__':
	print "wow?"










