import threading 
from time import sleep,time,ctime
loops = [4,2]

class ThreadFunc:

	def __init__(self,func,args,name=""):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		apply(self.func,self.args)


def loop(nloop,nsec):
	print "Start loop",nloop,"at",ctime(time())
	sleep(nsec)
	print "loop",nloop,"done at",ctime(time())

def main():
	print "starting threads..."
	threads = []

	nloops = range(len(loops))
	for i in nloops:
		t = threading.Thread(\
				target = ThreadFunc(loop,(i,loops[i]),
					loop.__name__))
		threads.append(t)
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()
	print "all DONE at",ctime(time())

if __name__ =="__main__":
	main()
