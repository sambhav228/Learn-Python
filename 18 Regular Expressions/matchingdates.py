import re

str = "Take up 1 1-03-2019 one 23 idea.One  567idea at a time 20-1-2021"

result = re.split(r'\d{1,2}-\d{1,2}-\d{4}', str)            # finds and removes dates
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)          # finds and prints dates okay
print(result)
