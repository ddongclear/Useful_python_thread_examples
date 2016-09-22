import time
import thread




def myfunction(string,sleeptime,lock,*args):
	while 1:
	#entring critical section
		lock.acquire()
		time.sleep(sleeptime)
		print string
		lock.release()
	#exiting critical section
		time.sleep(sleeptime)


if __name__ =="__main__":
	lock = thread.allocate_lock()
	thread.start_new_thread(myfunction,("Thread No : 1",2,lock))
	thread.start_new_thread(myfunction,("Thread No : 2",4,lock))

	while 1:
		pass
