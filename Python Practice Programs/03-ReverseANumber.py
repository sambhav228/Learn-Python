# Program to input a number and print it's reverse

n = int(input("Enter the number: "))
rev = 0
while(n>0):
    d = n%10
    rev = rev*10 + d
    n = n//10               # double slash because we want the integer output

print("Reverse of the number is:",rev)