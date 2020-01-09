import socket

HEADERSIZE = 10

#AF_INET, family type, corresponding to ipv4 and SOCK_STREAM to TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234)) #but usually the client is remote to the server

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16) # buffer
        if new_msg:
            print(f'new message length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE].decode()) #收到的一条完整msg的长度
            new_msg = False # 当前条msg还没接收（缓冲）完
        full_msg += msg.decode('utf-8')

        if len(full_msg) - HEADERSIZE == msglen:
            print('Full message received: ',full_msg[HEADERSIZE:])
            new_msg = True #又可以接收服务器新发的msg了
            full_msg = '' # empty out，同上
    print(full_msg)
    print()
#s.close()
