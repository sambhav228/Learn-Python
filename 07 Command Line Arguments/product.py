import sys

lst = sys.argv

                         # lst[0] is always the file path/name
                         # Passed Parameters are stored from lst[1] onwards

print("Product is :",int(lst[1])*int(lst[2]))         # by default passed parameters are a string, so we need to type cast it into int