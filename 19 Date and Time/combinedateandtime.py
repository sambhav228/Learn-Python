from datetime import *

d = date(2020,3,31)
t = time(19,35)

dt = datetime.combine(d,t)
print(dt)