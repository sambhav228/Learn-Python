'''Find Cube of numbers in a list using List Comprehensions'''

'''Using normal Programming'''
'''
lst = []
for i in range(1,11):
    lst.append(i ** 3)

print(lst)
'''

'''Using List Comprehension'''

lst = []
lst = [x**3 for x in range(1,11)]           # Syntax: lst = [expression for_loop if_condition_if_any]
print(lst)