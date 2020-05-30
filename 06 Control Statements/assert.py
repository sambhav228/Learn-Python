'''Assert is used to display errors if invalid input is given'''


x = int(input("Enter a number greater than 10: "))
assert x>10, "Wrong Number Entered"
print("You entered ",x)     # if the assert function is executed then this statement won't be executed