x = int(input("Enter a number for checking whether it's Prime or not"))

primeFlag = True

for i in range(2,x):
    if x%i == 0:
        primeFlag = False

if (primeFlag):
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")