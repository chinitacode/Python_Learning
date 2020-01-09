## tcp响应服务器，先设置重用、绑定并监听本地ip和端口，等待客户端连接；
## 当与客户端建立连接后，服务器打印显示客户端ip和端口，
## 同时将接收的客户端信息和'I get it!'传给客户端，
## 此时等待输入一个新的信息传给客户端。
import socket,time
host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)

while True:
    clientsock,clientaddr=s.accept()
    print("连接来自：",clientaddr)
    while True:
        data = clientsock.recv(4096) #阻塞方法
        if len(data.decode()) <= 1:
            break
        print('From client %s: %s' %(clientaddr,data.decode()))
        clientsock.sendall(data)
        clientsock.sendall("I get it!\n".encode())
        t = input('Send message to server here: ')
        clientsock.sendall(t.encode())
        time.sleep(1)
        #除非服务器给客户端发送空包：
        clientsock.send('c'.encode())
    clientsock.close()

'''
连接来自： ('169.254.197.163', 50310)
From client ('169.254.197.163', 50310): Hello server!
Send message to server here: Hello client

# 最后服务器和客户端都被自己阻塞在等待接收消息那，死锁。
'''
