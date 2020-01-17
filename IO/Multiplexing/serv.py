#服务端
from socket import *
import select
server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1',8093))
server.listen(5)
# 设置为非阻塞
server.setblocking(False)

# 初始化将服务端socket对象加入监听列表，后面还要动态添加一些conn连接对象，当accept的时候socket就有感应，当recv的时候conn就有动静
rlist=[server,]
rdata = {}  #存放客户端发送过来的消息

wlist=[]  #等待写对象
wdata={}  #存放要返回给客户端的消息

print('Server starts listening ...')
count = 0 #写着计数用的，为了看实验效果用的，没用
while True:
    # 开始 select 监听,对rlist中的服务端server进行监听，select函数阻塞进程，直到rlist中的套接字被触发
    #此例中，套接字接收到客户端发来的握手信号，从而变得可读，满足select函数的“可读”条件
    # 被触发的（有动静的）套接字（服务器套接字）返回赋给了rl里面；
    rl,wl,xl = select.select(rlist,wlist,[],1)
    print('次数 %s >>'%(count),rl)
    count = count + 1
    # 对rl进行循环判断是否有客户端连接进来,当有客户端连接进来时select将触发
    for sock in rl:
        # 判断当前触发的是不是socket对象, 当触发的对象是socket对象时,说明有新客户端accept连接进来了
        if sock == server:
            # 接收客户端的连接, 获取客户端对象和客户端地址信息
            conn,addr = sock.accept()
            print(f'Connected with {addr}')
            # 把新的客户端连接加入到监听列表中，当客户端的连接有接收消息的时候，select将被触发，会知道这个连接有动静，有消息，那么返回给rl这个返回值列表里面。
            rlist.append(conn)
        else:
            # 由于客户端连接进来时socket接收客户端连接请求，将客户端连接加入到了监听列表中(rlist)，客户端发送消息的时候这个连接将触发
            # 所以判断是否是客户端连接对象触发
            try:
                data = sock.recv(1024)
                #当客户端主动断开后就会发送''，所以没有数据的时候，我们将这个连接关闭掉，并从监听列表中移除
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    print(f'Client {sock} closed.')
                    continue
                print("Received {0} from client {1}".format(data.decode(), sock['rddr']))
                #将接受到的客户端的消息保存下来
                rdata[sock] = data.decode()

                #将客户端连接对象和这个对象接收到的消息大写加工成返回消息，并添加到wdata这个字典里面
                wdata[sock] = data.upper()
                #需要给这个客户端回复消息的时候，我们将这个连接添加到wlist写监听列表中
                wlist.append(sock) # 改变了select的input参数，只有下一轮select阻塞时wl才会有返回
            #如果这个连接出错了，客户端暴力断开了（注意，我还没有接收他的消息，或者接收他的消息的过程中出错了）
            except Exception:
                #关闭这个连接
                sock.close()
                #在监听列表中将他移除，因为不管什么原因，它毕竟是断开了，没必要再监听它了
                rlist.remove(sock)

    # 如果现在没有客户端请求连接,也没有客户端发送消息时，开始对发送消息列表进行处理，是否需要发送消息
    print('Outside of the select loop')
    for sock in wl:
        print(f'Sending {wdata[sock].decode()} to client {sock}')
        sock.send(wdata[sock])
        wlist.remove(sock)
        wdata.pop(sock)

    #将一次select监听列表中有接收数据的conn对象所接收到的消息打印一下
    for k,v in rdata.items():
        print(k,'发来的消息是：',v)
    #清空接收到的消息
    rdata.clear()
