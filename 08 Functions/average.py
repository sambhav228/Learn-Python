'''Printed the value from a Function'''
# def average(a,b):
#     print("Average pf two numbers is :",(a+b)/2)
#
# average(10,20)
#
# '''Return the value from a Function'''
# def average2(a,b):
#     return (a+b)/2
#
# avg = average2(10,20)
# print(avg)

'''Using keywords arguments'''

# def average(a,b):
#     print(a)
#     print(b)
#     return (a+b)/2
#
# print(average(b=10,a=20))           # this assigns value and the above printed variables are assigned the same values


'''Using default arguments'''

def average(a=10,b=40):               # Assigning default values to arguments
    print(a)
    print(b)
    return(a+b)/2

print(average())                      # Calling the function without passing arguments, now this works only when default values are assigned to the arguments
print(average(a=30))                  # Calling the function with only 1 argument passed, now this works only when default values are assigned to the arguments