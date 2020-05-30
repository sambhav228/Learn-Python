import socket

s = socket.socket()         # By default IPv4 and TCP/IP are there

s.connect(('localhost',4000))           # connect() takes input as a SET

msg = s.recv(1024)          # When client received the message for this first time

while msg:                  # As long as we are receiving the message
    print("Received:", msg.decode())
    msg = s.recv(1024)              # 1024 is the buffersize i.e. the no.of bytes we receive at a time

s.close()

'''To run this, we have to also run the server file at the same time'''