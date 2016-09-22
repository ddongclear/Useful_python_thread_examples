
import threading, time

class Printtime(threading.Thread):

	def __init__(self,interval):
		threading.Thread.__init__(self)
		self.interval = interval 

	def run(self):
		while 1:
			time.sleep(self.interval)
			print time.ctime(time.time())


t = Printtime(5)
t.start()

while 1 :
	pass

