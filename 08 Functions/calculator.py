def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return(x,y,z,u)             # Returns a Tuple

result = calc(10,5)
print(result)

'''Get the output in different lines'''

for i in result:
    print(i)