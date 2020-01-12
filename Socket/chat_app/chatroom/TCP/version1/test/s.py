from socket import *
import threading
address = gethostname()     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port = 12345             #监听自己的哪个端口
buffsize = 1024          #接收从客户端发来的数据的缓存区大小

s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(2)     #最大连接数
clients = []
flag = False

def findIndex(sock):
    index  = 0
    for c in clients:
        if c == sock:
            return index
        index = index + 1
    return 0

def transmit(sock):
    global clients, flag
    user_name = sock.recv(buffsize).decode()
    for c in clients:
        c.sendall(('User %s entered the chat room. Welcome!' % user_name).encode())
    while True:
        try:
            if flag: break
            msg = sock.recv(buffsize).decode()
            if msg == 'exit':
                for c in clients:
                    if c == sock: continue
                    c.sendall(('User %s left the chat room.' % user_name).encode())
                index = findIndex(sock)
                clients.pop(index)
                #sock.close()
                break
            for c in clients:
                if c == sock: continue
                c.sendall((user_name + ': ' + msg).encode())

        except Exception as e:
            print(e)
            break
    sock.close()

def exit():
    global clients, flag
    while True:
        try:
            command = input()
            if command == 'exit':
                for c in clients:
                    c.sendall(command.encode())
                print('Shutting dowm the chat room.')
                print('Closing socket...')
                flag = True
                clients = []
                s.close()
                print('Socket closed successfully.')
                break
        except:
            break




while True:
    if flag: break
    clientsock, clientaddress = s.accept()
    print('Connected from: ', clientaddress)
    clients.append(clientsock)
    t = threading.Thread(target = transmit, args=(clientsock,))  #t为新创建的线程
    t.start()
    e = threading.Thread(target = exit)
    e.start()


s.close()
#print('Socket closed successfully.')
