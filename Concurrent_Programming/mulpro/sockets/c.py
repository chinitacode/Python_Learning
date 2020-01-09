## tcp客户端,首先输入要给服务器发送的信息，
## 回车后会与服务器建立连接并发送该信息，同时打印打印显示“Message sent”；
## 然后得到服务器返回信息，打印后等待服务器向其发送信息（一直阻塞等待，直到收到服务器发送的空包）后退出。

import socket,sys
port = 12345
host = socket.gethostname()
data = input('Enter the message to send：')
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((host,port))
except:
    print('Failed to connect to the server！')
s.send(data.encode())
print('Message sent')

while True:
    buf = s.recv(4096) #阻塞方法
    if len(buf.decode()) <= 1:
        #如果收到空包，也给服务器发送空包
        s.send('c'.encode())
        break
    print('Received from server: ',buf.decode())

'''
Enter the message to send：Hello server!
Message sent
Received from server:  Hello server!
Received from server:
I get it!

Received from server:  Hello client

# 最后服务器和客户端都被自己阻塞在等待接收消息那，死锁。
'''
