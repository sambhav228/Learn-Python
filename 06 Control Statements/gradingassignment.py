maths = int(input("Enter the marks in Maths"))

phy = int(input("Enter the marks in Physics"))

chem = int(input("Enter the marks in Chemistry"))

if maths < 35 or phy < 35 or chem < 35:
    print("You are Failed!!")
else:
    average = (maths+phy+chem)/3
    if average<=59:
        print("Grade C")
    elif average<=69:
        print("Grade B")
    else:
        print("Grade A")


