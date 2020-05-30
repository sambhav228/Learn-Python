# Program to check whether a number is STRONG Number or not

# STRONG Number is a number whose sum of factorial of digits is equal to the original number itself
# For example: 145 is a STRONG Number
# 1! + 4! + 5! = 1 + 24 + 120 = 145

n = int(input("Enter the number: "))
num = n
tot = 0

while(num>0):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    tot = tot + f
    num = num//10
if(tot == n):
    print("STRONG Number")
else:
    print("Not a Strong Number")