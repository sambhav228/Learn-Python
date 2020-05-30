"""Tuples are like List that cannot be modified. We use circular brackets for them " () ".
Therefore, we cannot use the following functions with Tuple:
1) append()
2) extend()
3) insert()
4) remove()
5) clear()"""

"""
extend() Function: https://appdividend.com/2019/01/04/python-list-extend-example-tutorial/
"""


'''Use a Tuple'''
tpl=()              # Empty Tuple
print(tpl)
print(type(tpl))    # Tuple Type


tpl=(40)            # This is not a Tuple, this is just an Integer
print(tpl)
print(type(tpl))    # We need to place ',' after the element if we are using a single elements in a Tuple to make it a tuple like following


tpl=(40,)           # This is a Tuple
print(tpl)
print(type(tpl))    


tpl=(40,50, 10.5,"Anu")     # Tuple can have different types of values/elements
print(tpl)
print(type(tpl))   


print(tpl[3])       # Index of a Tuple


print(tpl*4)        # Repitition of elements in a Tuple


""" We cannot perform 'Slicing' on a Tuple, as we cannot modify it"""


# Count
print(tpl.count(40))

#  print(tpl*4.count(40))               This is an Invalid Syntac, so we cannot count '4' 40's in it, we have to do it indirectly


# Find Index of given element
print(tpl.index("Anu"))         # Prints index of the given element in the Tuple





"""List to Tuple"""
lst = [1,2,3.4,"Kittu"]
print(lst)
print(type(lst))
tpl1 = tuple(lst)       # Converting a List to a Tuple
print(tpl1)
print(type(tpl1))
