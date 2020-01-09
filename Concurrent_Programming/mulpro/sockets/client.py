from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect((gethostname(),8080))


while True:
    msg = input('>>: ').strip()
    if not msg: continue

    client.send(msg.encode())
    msg = client.recv(1024)
    print(msg.decode())
