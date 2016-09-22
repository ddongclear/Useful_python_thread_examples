

import thread
import time


def print_time(delay):
	cnt = 0
	while 1:
		time.sleep(delay)
		cnt+=1 
		print cnt

thread.start_new_thread(print_time,(1,))
thread.start_new_thread(print_time,(0.5,))



#time.sleep(1)
while (1):
	pass

