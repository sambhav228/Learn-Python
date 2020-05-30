# Factorial of a given number

def factorial(num):
    return 1 if (num==0 or num==1) else num*factorial(num-1)

num = 5
print("Factorial of ",num,"is",
factorial(num))