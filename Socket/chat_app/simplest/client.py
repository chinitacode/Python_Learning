'''
最简易版的聊天室客户端，仅用一个线程来收消息。

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
true = True

def rec(s):
    global true
    while true:
        try:  # 就算客户端方主动断开连接，收消息的线程仍会工作，但是因为socket连接已经从客户端断开，服务端此时消息发不过来会报错
            msg_received = s.recv(1024).decode()
            if msg_received == 'exit':
                true = False
                print('He/She has ended the conversation.')
                break
            if true:
                print('Him/Her:', msg_received)
        except:
            break # 线程终止

trd = threading.Thread(target = rec, args = (s,))
trd.start()
print('Client Thread rec started')


while true:
    msg_for_server = input()
    s.send(msg_for_server.encode())
    if msg_for_server == 'exit':  # 从客户端主动断开socket连接
        true = False
        print('You have ended the conversation.')
print('Closing socket from client')
s.close()
trd.join()
print('Closing Client Thread')
