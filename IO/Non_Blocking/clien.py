#客户端
import socket, os, time, threading

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1',8083))

# while 1:
#     res = ('%s hello' % os.getpid()).encode('utf-8')
#     client.send(res)
#     data = client.recv(1024)
#     print(data.decode('utf-8'))


#多线程的客户端请求版本
def func():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.connect(('127.0.0.1',8083))
    sk.send(b'hello')
    time.sleep(1)
    print(sk.recv(1024))
    #收完消息就关闭sk连接
    sk.close()

for i in range(10):
    threading.Thread(target = func).start()
