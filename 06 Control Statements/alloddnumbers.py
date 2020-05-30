min = int(input("Enter the minimum value:"))
max = int(input("Enter the maximum value:"))

x = min

if x%2 == 0: x+=1

while x<=max:
    print(x)
    x+=2