from threading import *

class EvenNumbers:

    def even(self):
        self.c = Condition()
        self.c.acquire()
        for i in range(1,101):
            if i%2==0:
                print(i)
        self.c.notify()
        self.c.release()

class OddNumbers:
    def odd(self):
        self.c = Condition()
        self.c.acquire()
        for i in range(1,101):
            if i%2==1:
                print(i)
        self.c.notify()
        self.c.release()

e = EvenNumbers()
o = OddNumbers()

t1 = Thread(target = e.even)
t2 = Thread(target = o.odd)

t1.start()
t2.start()


'''
Someone else's Program:

from threading import *



class MyThread:

    def displayEvenNumbers(self):

        i = 0

        while(i<=100 and i%2==0):

            print(i)

            i+=1

           

    def displayOddNumbers(self):

        l = 0

        while(l<=100 and l%2!=0):

            print(l)

            l+=1



k = 0

while(k<=100):

    print(k)

    k+=1



obj = MyThread()

t1 = Thread(target=obj.displayEvenNumbers)

t1.start()



t2 = Thread(target=obj.displayOddNumbers)

t2.start()



'''