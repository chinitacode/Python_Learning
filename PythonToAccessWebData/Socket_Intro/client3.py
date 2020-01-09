import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 8080))
#client.sendall('Hi from client! Nice to meet you!'.encode())

while True:
    data = client.recv(8)
    #print(f'Message from server is: {data.decode()}')
    print(data.decode(),end='') #Welcome to the server!
