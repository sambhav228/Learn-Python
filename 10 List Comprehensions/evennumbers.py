'''Find the even numbers in a list using List Comprehension'''

lst = [1,34,56,23,45,59,13,16]
lst2 = [x for x in lst if x%2 == 0]
print(lst2)


'''Find the even numbers between 1 to 20 using List Comprehension'''

'''without using if condition'''
lst3 = [x+1 for x in range(1,21,2)]               # used a common increment of 2
lst4 = [x for x in range(2,21,2)]
print(lst3)
print(lst4)

'''using if condition'''
lst5 = [x for x in range(1,21) if x%2 == 0]
print(lst5)