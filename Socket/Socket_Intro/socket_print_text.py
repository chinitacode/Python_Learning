import socket
# Creating a socket endpoint inside our computer but not yet connected. Returns an object
# AF_INET = Address Format Internet, the default value of family parameter
# SOCK_STREAM, the type parameter for TCP connection,
# which enables “sequenced, reliable, two-way, connection-based byte streams” over TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the object
mysock.connect(('data.pr4e.org', 80)) # the program makes a connection to port 80 on the server www.py4e.com
# encode()to convert python's string which in unicode to UTF-8 bytes
request = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode() #RFC7230
mysock.send(request)
msg = ''

while True:
    # Receiving upmost 512 characters each time
    data = mysock.recv(512) # the buffer, 2 to 4000 is recommended
    if len(data) < 1: # end of the file
        break
    msg += data.decode()

print(msg)
mysock.close() # Closing the two-way TCP connection




'''
while True:
    # Receiving upmost 512 characters each time
    data = mysock.recv(512) # the buffer, 2 to 4000 is recommended
    if len(data) < 1: # end of the file
        break
    print(data.decode(),end='') # end=''表示两次print间不留间隔

mysock.close() # Closing the two-way TCP connection
'''
