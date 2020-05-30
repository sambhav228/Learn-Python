'''Product of numbers in 2 different lists provided that both the list have same length'''


a = [1,2,3,4,5]
b = [6,7,8,9,10]

z = []
'''Using normal programming'''
'''
for i in range(len(a)):
    z.append(a[i]*b[i])

print(z)
'''

'''Using List Comprehension'''

z = [a[i]*b[i] for i in range(len(a))]
print(z)