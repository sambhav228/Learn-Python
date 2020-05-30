'''Generators return a sequence type. It is similar to 'range' type, but with it's own properties'''

'''Custom Generator is nothing but a range type'''

def customgen(x,y):         # range is passed
    while x<y:
        yield x
        x += 1

result = customgen(10,18)

print(result)       # Output: <generator object customgen at 0x000001CDE1332948>

print("Printing in different rows as follows: ")
for i in result: print(i)
"""
Output:  Printing in different rows as follows:
10
11
12
13
14
15
16
17
"""