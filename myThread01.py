import threading , time , random
from Queue import Queue

import sys

#sys.stdout.write()
CONSUMER_CNT = 10 
PRODUCER_CNT = CONSUMER_CNT / 2

q = Queue(10)

class myDo():

    def myfunc1(self):
        for x in range(1000):
            sys.stdout.write("{} \n".format(x))
            time.sleep(0.0)

        sys.stdout.write("{}\
                \n".format("*******************************************************************************************************"))
    def myfunc2(self):
        for x in range(1000):
            sys.stdout.write("{} \n".format(x))
            time.sleep(0.0)

        sys.stdout.write("{}\
                \n".format("*******************************************************************************************************"))

class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        something_to_do = myDo()
        something_to_do.myfunc1()

        for i in range(500):
            sys.stdout.write(" [%s] get %s \n" % (self.getName(),q.get()))
            time.sleep(0.0)

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1000):
            rint = random.randint(0,20)
            q.put(rint)
            sys.stdout.write("[%s] put %s -------------\n" % (self.getName(),rint))
            time.sleep(0.0)

if __name__ == "__main__":
    #Thread list
    con  = []
    pro  =  []

    for i in range(PRODUCER_CNT):
        pro.append(Producer())


    for x in range(CONSUMER_CNT):
        con.append(Consumer())

    for th in pro:
        th.start()

    for th in con:
        th.start()


    for th in con:
        th.join()

    for th in pro:
        th.join()


    print "Exit"



