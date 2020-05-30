import re

str = "Take up 1 One 23 idea.One  567idea at a time Only"

result = re.findall(r'O\w+',str)            # '+' - one or more repititions
print(result)

result = re.findall(r'O\w*',str)            # '*' - any number of repititions
print(result)

result = re.findall(r'O\w?',str)            # '?' - zero or one repititionn
print(result)

result = re.findall(r'O\w{2}',str)          # {m} - exact number of repititions
print(result)

result = re.findall(r'O\w{3}',str)
print(result)

result = re.findall(r'O\w{1,2}',str)        # a range from minimum to maximum no. of reptitions
print(result)