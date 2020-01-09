import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",9999))
true=True
def rec(s):
    global true
    while true:
        t=s.recv(1024).decode("utf8")  #客户端也同理
        if t == "exit":
            true=False
            print('He/She has ended the conversation.')
            break
        print('Him/Her:',t)
trd=threading.Thread(target=rec,args=(s,))
trd.start()
while true:
    t=input()
    s.send(t.encode('utf8'))
    if t == "exit":
        true=False
        print('You have ended the conversation.')
        
s.close()
