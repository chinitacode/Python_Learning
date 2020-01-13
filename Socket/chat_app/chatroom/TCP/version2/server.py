from socket import *
import threading, _thread

'''
[修订]：
1.在bind之前设置开启了端口复用；
2.将server端处理主动退出的exit线程从主线程的循环中删掉，
在一定义完就立马开启。
3.仍然是在exit线程最后调用_thread.interrupt_main方法来中断主线程的循环。

'''


address = gethostname()     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port = 12345             #监听自己的哪个端口
buffsize = 1024          #接收从客户端发来的数据的缓存区大小


s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #开启端口复用
s.bind((address,port))
s.listen(2)     #最大连接数
clients = []

def transmit(sock, addr, i):
    global clients
    user_name = sock.recv(buffsize).decode()
    for c in clients:
        c.sendall(('User %s entered the chat room. Welcome!' % user_name).encode())
    while True:
        try:
            msg = sock.recv(buffsize).decode()
            if msg == 'exit':
                for c in clients:
                    if c == sock: continue
                    c.sendall(('User %s left the chat room.' % user_name).encode())
                clients.remove(sock)
                sock.close()
                print('Disconnected with client %s from ' % (i), addr)
                return
            for c in clients:
                if c == sock: continue
                c.sendall((user_name + ': ' + msg).encode())
        except Exception as e:
            print(repr(e))
            break

def exit():
    global clients
    while True:
        try:
            command = input()
            if command == 'exit':
                for c in clients:
                    c.sendall(command.encode())
                    c.close()
                print('Shutting dowm the chat room.')
                clients.clear()
                print('Successfully emptied all users.')
                break
        except Exception as e:
            print('Exception from exit: ', repr(e))
            break
    _thread.interrupt_main()
    s.close()
    print('Socket closed from exit')
    return

e = threading.Thread(target = exit)
e.start()

i = 1
while True:
    #用try/excrpt来应对exit线程里的_thread.interrupt_main用KeyboardInterruptError来中断的机制
    try:
        print('Waiting to be connected with client %s ...'%(i))
        clientsock, clientaddress = s.accept()
        print('Connected with client: ', i, 'from', clientaddress)
        clients.append(clientsock)
        t = threading.Thread(target = transmit, args = (clientsock, clientaddress, i))  #t为新创建的线程
        t.start()
        i += 1
    except:
        print('Stop connecting with incoming clients')
        break

print('Connection ended.')
