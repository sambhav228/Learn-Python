from datetime import *
import time

ldates = []

d1 = date(2020,9,12)
d2 = date(2019,6,23)
d3 = date(2019,10,1)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(5)               # This stops the program execution for 5 seconds and then executes the lower part

for d in ldates:
    print(d)