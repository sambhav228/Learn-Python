from datetime import *

ldates = []

d1 = date(2020,9,12)
d2 = date(2019,6,23)
d3 = date(2019,10,1)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

for d in ldates:
    print(d)