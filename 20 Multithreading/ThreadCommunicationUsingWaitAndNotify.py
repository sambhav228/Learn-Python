'''Thread Communication with Condition() Class using wait and notify method. There is also notifyALl method, if more than 1 threads are waiting for a particular thread to complete it's task.'''

"""But this wait and notify can only be used under LOCK() Condition"""

from threading import *
from time import *

class Producer:

    def __init__(self):
        self.products = []
        self.c = Condition()

    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.products.append("Product "+str(i))
            sleep(1)
            print("Item Added")
        self.c.notify()
        self.c.release()

class Consumer:

    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout = 0)
        self.prod.c.release()
        print("Orders Shipped ", self.prod.products)



p = Producer()
c = Consumer(p)

t1 = Thread(target = p.produce)
t2 = Thread(target = c.consume)

t1.start()
t2.start()