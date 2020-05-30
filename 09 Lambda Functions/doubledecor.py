'''Decorator is a functions which takes a function as an inout and also returns a function,
by adding some more features or modifying the value, returned by the function which is taken as an input in decorator'''

'''This Program is made to double the number returned by a function'''

def decor(fun):
    def inner():
        result = fun()                      # Copying the passed function into a variable
        return result*2                     # Returning the modified value returned by the inner function, here we are returning a variable not a function, therefore we can modify it while returning
    return inner                            # Returning the inner function, it is not a variable, so we cannot modify it while returning

def num():
    return 5

resultFun = decor(num)                      # Here, we are'nt using 'num()', instead we are using 'num' because, we are just passing it as a parameter to another function 'decor', that means we aren't invoking the 'num' function

print("The double of the value returned by the function is:",resultFun())           # Here, we are invoking the num function using 'resultFun()' i.e. along with open and closed round brackets

# Output: The double of the value returned by the function is: 10

'''What if we do invoke the num function before and just prints the value of 'resultFun' '''            # cannot use four ' together at the end, need to give space between the 1 apostrophe and 3 apostrophe for closing the comment
resultFun = decor(num())

print("The double of the value returned by the function is:",resultFun)


# Output: The double of the value returned by the function is: <function decor.<locals>.inner at 0x00000231A0C83678>                # This is a bit different number each and every time we run the program, it's not unique