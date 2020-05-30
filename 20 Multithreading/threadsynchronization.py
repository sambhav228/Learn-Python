'''Thread Synchronization'''

'''Suppose, in an Airline Reservation system, we should avoid that two different people should not book the same seat.
To avoid that, we use thread synchronization.
We can use:
1) Lock()                           # mutex method i.e. a thread locks and acquires an object so that no other thread uses that object until it releases that object
or
2) Semaphore()                      # 1  ->   0   ->   1        # Similarly, acquire and release the lock
'''