'''We will be using RECURSION in this'''

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(7))