import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # The 2 arguments passed in parameters are optional, even if we do not pass anything, these 2 will be their by default

# AF_INET - tells to use IPv4 IP version 4 address
# SOCK_STREAM - it tells that the type of connection is TCP/IP

s.bind((host,port))         # bind() method takes a set as an input

print("Server listening on Port:", port)
s.listen(1)             # It tells that maximum 1 client is allowed,   it is the number of connections the server is going to accept

c,addr = s.accept()             # accept() method returns two things i.e. 1) Connection Object and 2) Address of Connection

print("Connection from:",str(addr))

c.send(b'Hello, how are you?')           # we need to encode this message into binary, so we are using 'b' just before message
# Alternate Method for send
c.send("Bye".encode())
c.close()