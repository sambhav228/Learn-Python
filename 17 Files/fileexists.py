import os, sys

if os.path.isfile('myfile.txt'):            # Change the file name to 'myfile123.txt' or anything else to test the program
    f = open('myfile.txt','r')              # Change the file name to 'myfile123.txt' or anything else to test the program
else:
    print('File does not exist.')
    sys.exit()

s = f.read()
print(s)
f.close()