import socket
import select

HEADER_LENGTH = 10
IP = '127.0.0.1'
port = 1234

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
