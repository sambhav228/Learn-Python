import sys

lst = sys.argv                      # This gives us the List of Command Line Arguments

for i in lst: print(i)              # Prints file path


 # Click on the "Run configurations" or "Edit Comfigurations" of your IDE and then in the 'Parameters' section pass "123 456 789". Now, you will get a length of 4

print(len(lst))


print(lst[0])               # Prints file path

print(lst[1])               # Prints "123", the first argument passed in 'Parameter' using "Edit Configurations"