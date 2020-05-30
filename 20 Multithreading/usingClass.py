'''Crate a thread using class i.e. without extending any parent class'''


from threading import *

class MyThread:
    def displayNumbers(self):
        i = 0
        while i<=10:
            print(i)
            i+=1

obj = MyThread()                    # Create an object of the class

t = Thread(target=obj.displayNumbers)           # Create a Thread object    Syntax: var = Thread(target = object.function_name,args)

t.start()                               # This starts the Thread