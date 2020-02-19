import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # the program makes a connection to port 80 on the server www.py4e.com
# encode()to convert python's string which in unicode to UTF-8 bytes
request = 'GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n'.encode() #RFC7230
mysock.send(request)
msg = ''

while True:
    # Receiving upmost 512 characters each time
    data = mysock.recv(10) # the buffer, 2 to 4000 is recommended
    if len(data) == 0: # end of the file
        print('Empty package received: ',data.decode())
        break
    msg += data.decode()

print(msg)
#mysock.close() # Closing the two-way TCP connection
