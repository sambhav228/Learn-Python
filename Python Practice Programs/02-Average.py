# Calculate Average of numbers in a given list:

n = int(input("Enter the number of elements to be entered in the list: "))
lst = []
for i in range(0,n):
    elem = int(input("Enter the element: "))
    lst.append(elem)

avg = sum(lst)/n

print("Average of numbers in the List is:",avg)
