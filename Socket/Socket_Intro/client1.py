import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 8080))
#client.sendall('Hi from client! Nice to meet you!'.encode())

from_server = ''
while True:
    data = client.recv(10)
    if len(data) < 1:
        break
    from_server += data.decode()
    print(data.decode(),end='')

#client.close()
print(f'Message from server is: {from_server}')
