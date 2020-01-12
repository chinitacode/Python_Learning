#客户端与上一个没有任何改变
from socket import *
import threading

address = gethostname()   #服务器的ip地址
port = 12345           #服务器的端口号
buffsize = 1024        #接收数据的缓存大小


s = socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
user_name = input('Please enter your user name: ')
s.sendall(user_name.encode())

def rec(sock):
    while True:
        try:
            msg_received = sock.recv(buffsize).decode()
            if msg_received == 'exit':
                print('Chat room closing...')
                break
            print(msg_received)
        except:
            break
    s.close()

t_rec = threading.Thread(target = rec, args = (s,))
t_rec.start()

while True:
    try:
        msg = input()
        s.sendall(msg.encode())
        if msg == 'exit':
            print('Exiting the chat room...')
            break
    except:
        break

s.close()
print('Chat room exitted successfully.')
