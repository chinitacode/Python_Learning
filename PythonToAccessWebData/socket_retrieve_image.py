import socket
import time


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = 'data.pr4e.org'
port = 80
s.connect((host,port))
request = 'GET /cover3.jpg HTTP/1.1\r\nhost: ' + host + '\r\n\r\n'
s.sendall(request.encode())
count = 0
picture = b''

while True:
    data = s.recv(5120) #buffer, receiving data up to 5120, dependending on the speed of data transmission, usually less than 5120
    if len(data) < 1: break
    time.sleep(0.25) # slow down our successive recv() calls, wait a quarter of a second after each call
    count += len(data)
    print(len(data),count)
    picture += data

s.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b'\r\n\r\n')
print('Header Length: ', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
#print(picture)
fhand = open('stuff.jpg','wb')
fhand.write(picture)
fhand.close()

'''
There is a buffer between the server making send() requests and our application
making recv() requests. When we run the program with the delay in place, at
some point the server might fill up the buffer in the socket and be forced to pause
until our program starts to empty the buffer. The pausing of either the sending
application or the receiving application is called “flow control.”
'''
