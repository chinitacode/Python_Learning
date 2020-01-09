'''
最简易版的聊天室服务端，仅用一个线程来收消息。只支持建立一个TCP socket连接。

[注意]：
1.socket连接的正常关闭（即双方都close）需要双方发送'exit'消息。

2.如果客户端主动断开，则服务端的收消息线程rec因为收到了'exit'消息所以跳出循环，终止线程，
但是主函数会因继续尝试给客户端发送消息而报错，因此主函数必须设置一个try/except捕捉exception；
但是客户端的收消息rec仍继续等待从已经断开了的socket收消息，则会报错，所以也必须设置try/except来避免bug。
同时因为服务端主函数的input()阻塞，所以服务端也该应该发出'exit'来正确地断开服务端这边的socket连接。

3.如果是服务端主动断开，即主函数因发送'exit'而break出来主动关闭socket，
则客户端的收消息线程rec也收到'exit'而终结，客户端的主函数也发送'exit'即可断开，
那么服务端收消息的rec线程收到'exit'则顺利终结线程。

'''

import socket, threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(2)
sock,addr = s.accept()
print(f'Connection from {addr} is established!')
true = True

def rec(sock):
    global true
    while true:
        msg_received = sock.recv(1024).decode()
        if msg_received == 'exit':  # 只要有一方发出'exit',都会断开socket连接
            true = False
            print('He/She has ended the conversation.') # 客户端方已断开连接
            break #线程终结
        if true:
            print('Him/Her:', msg_received)

#创建线程来专门接收消息, target是线程函数名，args是一个元祖，包含了传入该函数的参数，
# 即已经连接好了的socket
trd = threading.Thread(target = rec, args = (sock,))
trd.start()
print('Server Thread rec started')

#发送消息：
while true:
    msg_for_client = input()
    try: # 如果客户端主动断开连接，服务端仍继续发送消息则会报错，因为消息发不出去
        sock.send(msg_for_client.encode())
        if msg_for_client == 'exit':  # 服务端断开连接
            true = False
            print('You have ended the conversation.')
            break
    except: #当客户端突然断开连接的时候会报错
        break

print('Closing socket from server')
s.close()
