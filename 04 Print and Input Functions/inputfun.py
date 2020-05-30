s = input()
print(s)

s = input("Enter your Name:")
print(s)



i = input("Enter an Integer Number:")
print(i)
print(type(i))


i = int(input("Enter an Integer Number:"))
print(i)
print(type(i))



'''Reading Multiple Inputs'''
lst = [x for x in input("Enter three numbers separated by space:").split()]
print(lst)

lst = [x for x in input("Enter three numbers separated by comma:").split(',')]
print(lst)

lst = [int(x) for x in input("Enter three numbers separated by comma:").split(',')]
print(lst)

lst = [float(x) for x in input("Enter three numbers separated by comma:").split(',')]
print(lst)