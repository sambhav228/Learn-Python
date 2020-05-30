'''
\
.
^           -       searches from beginning
$
[...]
[^....]
(...)
(R | S)                     can use 2 regular expressions, either this or that will be executed
'''

import re

str = "Take up 1 1-03-2019 one 23 idea.One  567idea at a time 20-1-2021"


result = re.findall(r'^T\w*',str)
print(result)