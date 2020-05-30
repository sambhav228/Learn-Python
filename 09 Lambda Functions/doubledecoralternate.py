def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decorfun               # Using '@decorator_name" before the function that is to be called to pass the value to decorator, then we don't need to use "resultFun = decor(num)"
def num():
    return 5

print(num())