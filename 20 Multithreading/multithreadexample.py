'''Crate a thread using class i.e. without extending any parent class'''


from threading import *

class MyThread:
    def displayNumbers(self):
        i = 0
        print(current_thread().getName())
        while i<=10:
            print(i)
            i+=1

obj = MyThread()                    # Create an object of the class

t = Thread(target=obj.displayNumbers)           # Create a Thread object    Syntax: var = Thread(target = object.function_name,args)

t.start()                               # This starts the Thread


t2 = Thread(target=obj.displayNumbers)
t2.start()

t3 = Thread(target=obj.displayNumbers)
t3.start()

t4 = Thread(target=obj.displayNumbers)
t4.start()

'''The sequence of execution of all the thread depends totally on python thread scheduler, it is random according to us'''

'''Sometimes, it may give a proper output like first only thread-1 is executed then thread-2, then thread-3 and then thread-4'''