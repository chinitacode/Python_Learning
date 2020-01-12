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


def exit(i):
    global clients, flag
    while True:
        try:
            if flag: break
            command = input()
            if command == 'exit':
                for c in clients:
                    c.sendall(command.encode())
                #print('Shutting dowm the chat room.')
                flag = True
                clients.clear()
                print('Successfully emptied all users.')
                break
        except Exception as e:
            print('i = %s, Exception from exit: '%(i), repr(e))
            break
        s.close()
        print('Socket closed from exit')


i = 1
while True:
    try:
        if flag:
            print('Detecting flag being True while i = %s' % (i))
            break
        print('Waiting to be connected with client %s ...'%(i))
        clientsock, clientaddress = s.accept()
        print('Connected with client: ', i, 'from', clientaddress)
        clients.append(clientsock)
        t = threading.Thread(target = transmit, args=(clientsock, clientaddress, i))  #t为新创建的线程
        t.start()
        e = threading.Thread(target = exit, args=(i, ))
        e.start()
    except:
        print('Client %s Breaking due to exception!' % (i))
        break
    i += 1

s.close()
print('Socket closed in the end. i = %s' % (i))
