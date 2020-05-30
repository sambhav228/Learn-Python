x = 123             # global variable, can be accessed anywhere throughout the program

'''Accessing Global Variable with same name inside the function'''

def display():
    x = 678         # local variable with the same name as that of global variable
    print(x)
    print(globals()['x'])     # accessing global variable with the same name as that of local variable

print(x)        # accessed global variable

display()       # called the function


'''Assigned function to a variable'''
z = display

z()     # Reusing the variable to call the function as many times as wanted
z()
z()