x = int(input("Enter a number"))

for i in range(0,x):
    i+=1
    if i == 101:
        break
    if i%10 == 0:
        continue
    print(i)

