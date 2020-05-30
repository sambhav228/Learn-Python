'''Use Filter function to display only the even numbers from a list'''


lst = [14,23,45,23,46,68,20]

result = filter(lambda x : x%2 == 0, lst)                 # Prints the filter object              Output: <filter object at 0x0000027DF835DB88>

result2 = list(filter(lambda x : x%2 == 0, lst))          # To get the output like a list         Output: [14, 46, 68, 20]

print(result)

print(result2)