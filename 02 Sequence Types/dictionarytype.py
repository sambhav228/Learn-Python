'''Dictionary is a key-value pair. It has keys not index. We can use keys as integers or as strings too'''


# Create a Dictionary
dict1 = {1:'Anubhav',2:'Digant',3:'Deep',4:'Tamta',5:'Madhav'}
print(dict1)
# Output: {1: 'Anubhav', 2: 'Digant', 3: 'Deep', 4: 'Tamta', 5: 'Madhav'}


# Creating Dictionary with character as a key
# dict2 = {a:1,b:33,c:45}       # key should be within single quotes if it is a character
# print(dict2)

dict2 = {'a':1,'b':33,'c':45}
print(dict2)                # Output: {'a': 1, 'b': 33, 'c': 45}

# Creating Dictionary with string as a key
dict3 = {'anu':1,'bha':33,'ckl':45}
print(dict3)                # Output: {'anu': 1, 'bha': 33, 'ckl': 45}



# Show all the items in a Dictionary
print(dict1.items())        # Output: dict_items([(1, 'Anubhav'), (2, 'Digant'), (3, 'Deep'), (4, 'Tamta'), (5, 'Madhav')])


# Get all the keys of a Dictionary
k = dict3.keys()            # Prints all the keys of the dictionary
for i in k: 
    print(i)
    
    
# Get all the values of a Dictionary
v = dict3.values()          # Prints all the values of the dictionary
for i in v:
    print(i)
    
    
    
# Accessing element of a dictionary using it's key
print(dict1[3])             # '3' is the "key" of dictionary, it's not the index


# Delete the elements of a Dictionary using it's key
print(dict1)
del dict1[5]
print(dict1)