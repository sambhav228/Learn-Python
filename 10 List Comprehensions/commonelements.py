'''Finding Common Elements in 2 different List using List Comprehension'''

a = [1,2,3,4,5]
b = [2,4,6,8]
result=[]

'''Using Normal Programming'''
'''
for i in a:
    if i in b:                      # This method in python checks that whether the 'i' in 'a' is in 'b' or not
        result.append(i)

print(result)
'''

'''Using List Comprehensions'''

result = [i for i in a if i in b]
print(result)