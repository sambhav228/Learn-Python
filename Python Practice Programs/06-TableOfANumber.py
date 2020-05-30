# Program to print the table of a number

n = int(input("Enter the number: "))
print("Table of the given number:")
for i in range(1,11):
    print(n,'*',i,'=',n*i)