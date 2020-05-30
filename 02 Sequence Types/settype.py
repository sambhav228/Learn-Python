""" Set do not allows duplicate elememts. We use curly braces for them ' { } '.
We can enter elements of all datattypes in a Set.
"""

# Create a Set
s = {10,20,3.4,"Madhav"}        
print(s)                       # Always prints in a random order
print(type(s))

# Removing an element from a Set
s.remove(10)
print(s)

# Duplicacy of elements is just omitted/ignored
s = {10,20,7.9,"Madhav",10,20,10}
print(s)
print(type(s))


# Add new elements to a Set
s.update([1,23,87,"Kittu"])         # Added elements are also printed in a random order
print(s)

# Trying Updating Set Directly while Printing
s = {10,20,7.9,"Madhav",10,20,10}
print(s.update([15]) )    # ouputs "None" and do not ouputs '15' as an added element to the set


# Set do not supports Indexing
# print(s[1])               # This shows an error, cause set do not follows any order, thus have no indexing
 
 
# Set is not subscriptable
# print(s[0:5])             # This shows an error, i.e. Set cannot be sliced or sunscripted, because it do not follows any order or indexing


# Repitition of elements in a Set
# print(s*3)                  # This shows an error, i.e. Repitition is not allowed in a Set because it do not allows duplicate elements



# Removing Elements from a Set
# s.remove(1)                               # It is also not working, not sure about it.
# print(s)



# print(s.remove("Kittu"))



'''Frozen Set'''
''' We cannot update() or remove() elements from a Frozen Set. We can just navigate and print the elements from a Frozen Set using a for loop'''

# Set to FrozenSet
s1 = {1,2,3,335,6.7,'Anubhav'}
f = frozenset(s1)               # Converting a Set to a Frozen Set
print(f)                        # Output: frozenset({1, 2, 3, 6.7, 'Anubhav', 335})

# f.update(5)                   #  Shows error because AttributeError: 'frozenset' object has no attribute 'update'

# f.remove(2)                   #  Shows error because AttributeError: 'frozenset' object has no attribute 'remove'



