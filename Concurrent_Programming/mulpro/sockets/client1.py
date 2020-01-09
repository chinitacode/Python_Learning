from socket import *
from multiprocessing import Process

def conn(server,num):
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(server)
    while True:
        msg = 'From client' + str(num) + ': Hello server!'
        if not msg: continue
        client.send(msg.encode())
        msg = client.recv(1024)
        print(msg.decode())

if __name__ == '__main__':
    for i in range(20):
        c = Process(target=conn, args=((gethostname(),8080),i))
        print('Client %s connecting to server ...' %i)
        c.start()
