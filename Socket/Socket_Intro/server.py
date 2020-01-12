import socket
import time

# 必须加一个HEADER来告知client所穿送的消息的长度！
HEADERSIZE = 10

#AF_INET, family type, corresponding to ipv4 and SOCK_STREAM to TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5) # a queue of 5

while True:
  # socket object  # the source ip address of info coming from
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!") # debugging string

    msg = 'Welcome to the server!'
    msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, 'utf-8')) # send message to client socket
    #bytes('','utf-8') == b'' == ''.encode()
    #clientsocket.close() #因为是Stream连接，所以理论上server是一直在发送数据的，
                         #类似于一个rest API, 也就是说当server不断开连接前，client是无法收数据的。
    while True:
        time.sleep(3)
        msg = f'The time is: {time.time()}'
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, 'utf-8'))

'''
[socket.listen(backlog)]
listen里有个参数backlog是指定tcpsever可以同时接受多少个客服端的连接申请，当超过此数时server将拒绝客户端的连接申请，
给出socket.error: [Errno 10061]错误。
tcp的server尽管可以同时接受n个客服端连接，但只能和第一个连接的客服端互相通信，
当第一个tcp连接的客户端关闭后才能和第二个连接申请的客户端通信，即后边的被阻塞了，一次只能和一个tcp客户端进行通信。

socket.listen(backlog)
backlog指定最多允许多少个客户连接到服务器。它的值至少为1。
收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求。

backlog应该理解为阻塞队列的长度，总共与服务器连接的客户端一共有 backlog + 1 个。
阻塞队列FIFO，当连接客户端结束后阻塞队列里的第一个客服端与服务器连接成功。

socket.listen(n)
简单来说，这里的nt表示socket的”排队个数“

一般情况下，一个进程只有一个主线程（也就是单线程），那么socket允许的最大连接数为: n + 1
如果服务器是多线程，比如上面的代码例子是开了2个线程，那么socket允许的最大连接数就是: n + 2
换句话说：排队的人数(就是那个n) + 正在就餐的人数（服务器正在处理的socket连接数) = 允许接待的总人数（socket允许的最大连接数）

'''
