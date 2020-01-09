import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",9999))
s.listen(2)
sock,addr=s.accept()
print(f'Connection from {addr} is established!')
true=True

def rec(sock):
    global true
    while true:
        t = sock.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法
        if t == "exit":
            true = False
            print('He/She has ended the conversation.')
            break
        print('Him/Her:',t)
trd=threading.Thread(target=rec,args=(sock,))
trd.start()
while true:
    t=input()
    sock.send(t.encode('utf8'))
    if t == "exit":
        true=False
        print('You have ended the conversation.')

print('Closing socket from client')
s.close()
