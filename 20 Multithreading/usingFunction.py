'''Create first Thread using function'''

from threading import *

def displayNumbers():
    i = 0
    print(current_thread().getName())           # This is Thread-1
    while i<=10:
        print(i)
        i+=1


print(current_thread().getName())               # This is Main() Thread
t = Thread(target=displayNumbers)               # Syntax: var = Thread(target=function_name,args)

t.start()                                       # This starts the thread

