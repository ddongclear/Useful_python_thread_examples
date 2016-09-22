


import threading

date = []

lck = threading.Lock()

def put_obj(obj):
	lck.acquire()
	data.append("object")
	lck.release()

def get_obj():
	lck.acquire()
	r = data.pop()
	lck.release()
	return r


