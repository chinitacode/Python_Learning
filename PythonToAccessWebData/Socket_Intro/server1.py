import socket
import time

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((socket.gethostname(), 8080))
serv.listen(5)

while True:
    clientsocket, addr = serv.accept() #clientsocket就是接下来通信（send和recv方法）的终端
    print(f'Connection from client {addr} is established!')
    clientsocket.sendall("Welcome to the server!\n".encode())
    #clientsocket.close() #只有server主动关闭连接，那么client就可以处理在recv的while循环外的总接收的数据
                         #否则client就成了阻塞线程，会继续一直等待server发送新数据

    while True:
        time.sleep(1)
        clientsocket.sendall(f"Now the time is: {time.time()}\r\n".encode()) #如果消息之间不加换行符，
                                                    # client那里的print就只能一直buffing，等server主动断开后一次性print出来
