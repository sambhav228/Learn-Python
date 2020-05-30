
"""Create a List"""
# Declaring a List
l1 = [1,2, 'Anubhav', 10.5, -30]


# Print a List
print(l1)

# Print element of a List at given Index
print(l1[3])

# Slicing a List
print(l1[3:5])

# Repitition in a List
print(l1*4)

# Length of a List
print(len(l1))





"""Adding and Removing List Elements"""
# Append an element
l1.append(40)           # will add the element at the end of List

# Remove an element 
l1.remove("Anubhav")    # removes "Anubhav" from l1

# delete an element through it's index by passing the list "del" function
del(l1[1])              # it is not a function for list, it is an inbuilt function in python in which we can pass a list or anything else

print(l1)






"""Few More List Functions"""

# Clear
"""l1.clear()          # Removes all the elements from the List and makes it empty
 print(l1) """
# commenting it for further purpose of List


# Maximum and Minimum of a List
print(max(l1))
print(min(l1))


# Insert an element at a given Index
l1.insert(3,99)             # shifts the element already at given index to right of it
print(l1)       


l1.insert(10,1001)          # If the index entered is invalid, then the element to be added is added at the last or at the end of list
print(l1)      




# Sort the elements.................works only when al the elements are of similar datatype

l1.sort()       # Ascending Order
print(l1)


l1.sort(reverse=True)       # Descending Order
print(l1)


l2 = ['Anubhav','Madhav','Deep']        #  all elements here can be compared...therefore, sort will work
l2.sort()
print(l2)