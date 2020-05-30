# Program to check whether a number is Palindrome or not

n = int(input("Enter the number: "))
num=n
rev = 0
while(n>0):
    d = n%10
    rev = rev*10 + d
    n=n//10

if(num==rev):
    print("Palindrome")
else:
    print("Not Palindrome")