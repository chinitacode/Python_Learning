import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 8080))
#client.sendall('Hi from client! Nice to meet you!'.encode())

data = client.recv(1024)
print(f'Message from server is: {data.decode()}')

'''
当client.recv()参数足够大，比如1024
不需要缓冲接收数据时就可以打印接收到完整的数据；
但是如果设置为8，接收不完整时，
只打印接收到的这8个characters
'''
