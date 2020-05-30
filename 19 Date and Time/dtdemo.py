'''epoch - time or total numbers of seconds held since your system was started. For all UNIX, it is around 1970'''


import time

epochseconds = time.time()      # Total number of seconds since your system started

print(epochseconds)


t = time.ctime(epochseconds)    # Tell us current date and time by calculating it using epochseconds
print(t)