'''Decorating Strings'''
def decor(fun):
    def inner(n):
        result = fun(n)
        result += " How are you?"
        return result
    return inner

@decor
def Hello(name):
    return "Hello " + name

print(Hello("Anubhav"))


# Output: Hello Anubhav How are you?