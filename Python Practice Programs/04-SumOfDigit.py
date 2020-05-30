# Program to input a number and find it's sum of digits


n = int(input("Enter the number: "))
tot = 0

while(n>0):
    d = n%10
    tot = tot+d
    n=n//10

print("Sum of Digits is:",tot)