'''Returning a Function'''

def display():
    def message():
        return "Hello Anubhav"
    return message                  # returning a function

fun = display()                     # function to a variable

print(fun())                        # invoking the function and printing it


