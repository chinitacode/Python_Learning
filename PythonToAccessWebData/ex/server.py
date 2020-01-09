import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(2)
sock,addr = s.accept() #一次只能连接一个客户端
print(f"Connection from {addr} has been established!")

while True:
    message = sock.recv(1024).decode() #服务端先接收信息
    if message == 'exit':
        break
    print(message)
    msg_for_client = input()  # 由于input函数的阻塞作用,以上的代码发完一条信息，只能等待另一端的信息发过来才能继续发送。
    if msg_for_client == 'exit': #服务端也可向客户端发送信息，但是必须在接收信息后才可以发送一次
        break
    sock.send(msg_for_client.encode())

s.close() #任意一方都可以发送'exit'断开连接
