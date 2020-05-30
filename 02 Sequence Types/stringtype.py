# Create a String
s= "I am Anubhav"
print(s)

# Multi Line String
s1 = """I am  Anubhav
I am a very good boy.
I am a Computer Science Engineer"""
print(s1)

# Index of a String
print(s[2])

# Print a String 2 times
print(s*2)

# Print a String 3 times
print(s1*3)

# Print the character at index 3 of a String 2 times
print(s[3]*2)

# Length of a String
print(len(s))
print(len(s1))




"""Slicing a String"""
# Something like SubString in Java

# Slicing a String
print(s[0:5])       # do not counts the elements at last index mention i.e.'5'

print(s[0:])        # counts till the last

print(s[:8])        # counts from the beginning

print(s[-3:-1])     # '-1' represents the last element. Here, it is 'v' and '-3' is 'h'. Also, it won't count the last elements, therefore only "ha"



# Steps in Slicing
print(s[0:9:2])     # from 0 to 8 with the gap of '1'

print(s[0:9:3])     # from 0 to 8 with the gap of '2'


print(s[15::-1])    # from end to beginning i.e. in reverse with no gap. Also, completely reversed the String

print(s[15::-2])    # from end to beginning i.e. in reverse order with a gap of '1'


# Reversing a String using Slicing
print(s[::-1])      



"""Stripping the Spaces"""
# kind of Trim() in Java

s2 = " Hello Anubhav "

print(s2)               # Prints String with spaces on both left and right of it

print(s2.strip())       # Removes the spaces from both sides of the String

print(s2.lstrip())      # Removes the space only from left side of the String

print(s2.rstrip())      # Removes the space only from right side of the String






"""Few More String Methods"""



# Find a character or Substring
print(s.find("Anu"))        # Prints the Starting Index of the searched SubString

print(s.find("ANU"))        # It's Case Sensitive, so no result i.e. '-1'

print(s.find("Anu",2,6))    # ("String to be searched", start_index_for_search, end_index_for _search)

print(s.find("Anu",2,8))    # SubString is Found



# Count 
print(s.count('a'))         # It is also Case Sensitive

print(s.count('Anu'))



# Replace
print(s.replace("am",'amm'))



# Upper, Lower and Title Case
print(s.upper())

print(s.lower())

print(s.title())        # 1st letter of each word is capital, rest is small



