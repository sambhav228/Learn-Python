try:
    a,b = [int(x) for x in input("Enter two numbers:").split()]
    c = a/b
    print(c)

except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")

print("Code after that exception")