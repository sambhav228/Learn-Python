'''Sum up all the numbers in a list using REDUCE Function'''

from functools import reduce                    # Reduce function should always ne imported from 'functools' library

lst = [10,5,20,15]

result = reduce(lambda x,y : x+y , lst)         # 'REDUCE' do not returns object like 'MAP' and 'FILTER'. It returns only 1 value whereas 'FILTER' and 'MAP' returns a sequence

print("Sum of the digits in the list is:",result)