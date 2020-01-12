# client.py

# 导入系统模块
import os, sys
# 导入网络编程（传输层）模块
from socket import *
# IO多路复用模块
from select import select
# 设置模块
from settings import *
# 语言模块
from language import *

def main():
    'main 主函数'
    client = socket(AF_INET, SOCK_STREAM)  # 建立TCP套接字

    # 登录函数
    if login(client):
        # 连接函数
        connect(client)

def connect(client):
    'connect 客户端连接函数'

    # 使用select模块的select方法实现IO多路复用监听传输
    rlist = [client, sys.stdin]
    wlist = []
    xlist = []

    while True:
        rs, ws, xs = select(rlist, wlist, xlist)

        for r in rs:
            if r is client:
                # 接受服务器发来的消息
                data = client.recv(buffersize)
                if data.decode() == '\n':
                    # 如果消息为回车，聊天室关闭
                    client.close()
                    print(txt_administrator_close_chatroom)
                    os._exit(0)
                else:
                    # 打印接收到的信息
                    print(data.decode(), end='')
            elif r is sys.stdin:
                # 发送消息给服务器
                data = sys.stdin.readline()
                if data == '\n':
                    # 如果回车，发送退出消息，关闭客户端，退出聊天室
                    data = curuser + ': ' + txt_user_quit_chatroom + '\n'
                    client.send(data.encode())
                    client.close()
                    os._exit(0)
                else:
                    # 发信息给服务器
                    data = curuser + ': ' + data
                    client.send(data.encode())

def login(client):
    '登录函数 login'
    # 使用全局变量管理用户
    # 先让客户端输入姓名
    global curuser
    curuser = input(txt_username)
    # 再连接到服务器，传送用户名以检验
    client.connect(ADDR)  # 连接到服务器地址
    print(txt_connect_to, ADDR)
    client.send(curuser.encode())
    data = client.recv(buffersize)
    if data.decode() == 'Username already exists!':
        # 如果用户名已经存在，要求重新输入
        print(txt_user_already_exists)
        return False
    else:
        # 发送信息给服务器，告知服务器用户进入聊天室
        # -*- 因为监听传输的是sys.stdin.readline()，所以必须在最后添加换行符，以便清除阻塞 -*-
        data = curuser + ': ' + txt_uesr_enter_chatroom + '\n'
        client.send(data.encode())
        return True


if __name__ == '__main__':
    main()
