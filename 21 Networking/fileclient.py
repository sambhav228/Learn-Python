''' This will send to the server the name of the file it wants and will display it's content on the command line/terminal'''

import socket

s = socket.socket()         # By default IPv4 and TCP/IP are there

s.connect(('localhost', 6767))           # connect() takes input as a SET

fileName = input("Enter the name of the file you want:")

s.send(fileName.encode())

content = s.recv(8192)

print(content.decode())

s.close()

'''To run this, we have to also run the server file at the same time'''