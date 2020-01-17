# 服务端
import socket, time


server=socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8083))
server.listen(5)

server.setblocking(False) #设置不阻塞
r_list=[]  #用来存储所有来请求server端的conn连接
w_list={}  #用来存储所有已经有了请求数据的conn的请求数据

while True:
    try:
        conn,addr = server.accept() #不阻塞，会报错
        print(f'Connected with {addr}!')
        #为了将连接保存起来，不然下次循环的时候，上一次的连接就没有了
        r_list.append(conn)
    except BlockingIOError:
        # 强调强调强调：！！！非阻塞IO的精髓在于完全没有阻塞！！！
        time.sleep(0.5) # 打开该行注释纯属为了方便查看效果
        print('在做其他的事情')
        print('rlist: ',len(r_list))
        print('wlist: ',len(w_list))


        # 遍历读列表，依次取出套接字读取内容
        del_rlist=[] #用来存储删除的conn连接
        for conn in r_list:
            try:
                data = conn.recv(1024) #不阻塞，会报错
                if not data: #当一个客户端暴力关闭的时候，会一直接收b''，别忘了判断一下数据
                    conn.close()
                    print('%s already closed!' % conn)
                    del_rlist.append(conn)
                    continue
                print('Data received: ',data.decode())
                w_list[conn] = data.upper() # 相当于conn收到的请求数据是小写，但是再由服务器回应时就把大写的数据发给conn
            except BlockingIOError: # 没有收成功，则继续检索下一个套接字的接收
                print(f'BlockingIOError from r_list')
                continue
            except ConnectionResetError: # 当前套接字出异常，则关闭，然后加入删除列表，等待被清除
                print('%s closed by ConnectionResetError!' % conn)
                conn.close()
                del_rlist.append(conn)

        print('del_rlist: ',len(del_rlist))
        print('wlist: ',len(w_list))
        # 遍历写列表，依次取出套接字发送内容
        del_wlist = []
        for conn,data in w_list.items():
            try:
                print(f'Sending {data.decode()} to {conn}')
                conn.send(data) # 由服务器回应时就把大写的数据发给conn
                del_wlist.append(conn)
            except BlockingIOError:
                print(f'BlockingIOError from w_list')
                continue
        print('del_wlist: ',len(del_wlist))


        # 清理无用的套接字,无需再监听它们的IO操作
        print('Clearing closed conn in r_list and del_rlist')
        for conn in del_rlist:
            r_list.remove(conn)
        del_rlist.clear() #清空列表中保存的已经删除的内容
        print('Clearing closed conn in w_list and del_wlist')
        for conn in del_wlist:
            w_list.pop(conn)
        del_wlist.clear()

        '''
        在做其他的事情
        rlist:  0
        wlist:  0
        del_rlist:  0
        wlist:  0
        del_wlist:  0
        Clearing closed conn in r_list and del_rlist
        Clearing closed conn in w_list and del_wlist
        Connected with ('127.0.0.1', 50918)!
        Connected with ('127.0.0.1', 50917)!
        Connected with ('127.0.0.1', 50920)!
        Connected with ('127.0.0.1', 50919)!
        Connected with ('127.0.0.1', 50921)!
        在做其他的事情
        rlist:  5
        wlist:  0
        Data received:  hello
        Data received:  hello
        Data received:  hello
        Data received:  hello
        Data received:  hello
        del_rlist:  0
        wlist:  5
        Sending HELLO to <socket.socket fd=304, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50918
        )>
        Sending HELLO to <socket.socket fd=308, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50917
        )>
        Sending HELLO to <socket.socket fd=356, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50920
        )>
        Sending HELLO to <socket.socket fd=352, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50919
        )>
        Sending HELLO to <socket.socket fd=360, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50921
        )>
        del_wlist:  5
        Clearing closed conn in r_list and del_rlist
        Clearing closed conn in w_list and del_wlist
        Connected with ('127.0.0.1', 50925)!
        Connected with ('127.0.0.1', 50922)!
        Connected with ('127.0.0.1', 50924)!
        Connected with ('127.0.0.1', 50923)!
        Connected with ('127.0.0.1', 50926)!
        在做其他的事情
        rlist:  10
        wlist:  0
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        Data received:  hello
        Data received:  hello
        Data received:  hello
        Data received:  hello
        Data received:  hello
        del_rlist:  5
        wlist:  5
        Sending HELLO to <socket.socket fd=364, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50925
        )>
        Sending HELLO to <socket.socket fd=368, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50922
        )>
        Sending HELLO to <socket.socket fd=372, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50924
        )>
        Sending HELLO to <socket.socket fd=376, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50923
        )>
        Sending HELLO to <socket.socket fd=380, family=AddressFamily.AF_INET, type=Socke
        tKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8083), raddr=('127.0.0.1', 50926
        )>
        del_wlist:  5
        Clearing closed conn in r_list and del_rlist
        Clearing closed conn in w_list and del_wlist
        在做其他的事情
        rlist:  5
        wlist:  0
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        <socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOC
        K_STREAM, proto=0> already closed!
        del_rlist:  5
        wlist:  0
        del_wlist:  0
        Clearing closed conn in r_list and del_rlist
        Clearing closed conn in w_list and del_wlist
        在做其他的事情
        rlist:  0
        wlist:  0
        del_rlist:  0
        wlist:  0
        del_wlist:  0
        Clearing closed conn in r_list and del_rlist
        Clearing closed conn in w_list and del_wlist
        Traceback (most recent call last):
          File "serv.py", line 16, in <module>
            conn,addr = server.accept() #不阻塞，会报错
          File "F:\python\lib\socket.py", line 212, in accept
            fd, addr = self._accept()
        BlockingIOError: [WinError 10035] 无法立即完成一个非阻止性套接字操作。

        During handling of the above exception, another exception occurred:

        Traceback (most recent call last):
          File "serv.py", line 22, in <module>
            time.sleep(0.5) # 打开该行注释纯属为了方便查看效果
        KeyboardInterrupt

        '''
