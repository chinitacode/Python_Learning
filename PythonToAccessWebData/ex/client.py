import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True:
    msg_for_server = input()  # 由于input函数的阻塞作用,以上的代码发完一条信息，只能等待另一端的信息发过来才能继续发送。
    s.send(msg_for_server.encode())  #客户端先发信息
    if msg_for_server == 'exit':
        break
    msg_received = s.recv(1024).decode()
    if msg_received == 'exit':
        break
    print(msg_received)

s.close()
