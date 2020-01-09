import socket
import pickle

# 必须加一个HEADER来告知client所穿送的消息的长度！
HEADERSIZE = 10

#AF_INET, family type, corresponding to ipv4 and SOCK_STREAM to TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5) # a queue of 5

while True:
  # socket object  # the source ip address of info coming from
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!") # debugging string

    d = {'name': 'Bob', 'age': 20, 'score': 88}
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

    clientsocket.send(msg) # send message to client socket
    #bytes('','utf-8') == b'' == ''.encode()
    #clientsocket.close() #因为是Stream连接，所以理论上server是一直在发送数据的，
                         #类似于一个rest API, 也就是说当server不断开连接前，client是无法收数据的。
