'''Double the values of all the elements of a list using MAP Function'''

lst = [2,3,4,5]

result = map(lambda n: n*2, lst)                       # Output: <map object at 0x0000029854675188>

result2 = list(map(lambda n: n*2, lst))                # Output: [4, 6, 8, 10]

print(result)

print(result2)