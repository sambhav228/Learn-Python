'''Sequence Characters: \d \D \s \S \w \W \b \A \Z'''

import re

str = "Take up 1 one 23 idea.One  567idea at a time"
# Now, we want a sub-string which has it's first letter as 'o' and is followed by any 2 characters
result = re.search(r'o\w\w',str)            # 'str' is the string in which we want to search for the substring
print(result.group())           # group() method is used only for the results of search() method and can be used with match() method too

result = re.findall(r'o\w\w',str)           # It returns a list of all found substrings
print(result)

result = re.match(r'o\w\w', str)            # match() method only works on the beginning of the String, i.e. it starts with the first word and gives out the first result whichever it matches
print(result)

result = re.match(r'T\w\w', str)
print(result)

result = re.match(r'T\w\w', str)
print(result.group())


'''
Output:
one
['one']
None
<re.Match object; span=(0, 3), match='Tak'>
Tak
'''

 # We cannot use the group() method if the result returned is 'None'

# Split a given string into multiple strings and returns a list
result = re.split(r'\d+', str)         # 'd' is digit and '+' is more than 1 digit          # split() - removes the substring mentioned in regular expression
print(result)               # Output: ['Take up ', ' one ', ' idea.One  ', 'idea at a time']

result = re.sub(r'idea','Time',str)         # substitute - sub() replaces all the substrings with the given string according to the regular expression passed
print(result)