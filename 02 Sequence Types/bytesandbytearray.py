'''bytes and bytearray both do not supports slicing and repitition'''


# Convert a List to bytes
lst = [1,2,3,234]       # bytes cannot be more than '255'
print(lst)
print(type(lst))

b = bytes(lst)          # Converting a List to create bytes
print(b)                # OutPut: b'\x01\x02\x03\xea'
print(type(b))          # OutPut: <class 'bytes'>

# Length of bytes
print(len(b))


# Adding or modifying elements to a byte shows an error
# b[3] = 22               # TypeError: 'bytes' object does not support item assignment



# Convert a List to bytearray

b1 = bytearray(lst)
print(b1)               # OutPut: bytearray(b'\x01\x02\x03\xea')
print(type(b1))         # OutPut: <class 'bytearray'>


# Adding or modifying elements is allowed in a bytearray
b1[3]=22
print(b1)

# Length of bytearray
print(len(b1))

# b1[5] = 35            # Error: IndexError: bytearray index out of range
# Similarly,
# b1[8]=45              # This shows an error because we cannot add element at 8th index as bytearray is only of size 4

