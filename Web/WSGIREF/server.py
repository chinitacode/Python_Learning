# server.py
# make a simple server using wsgiref module of python

from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 在 git bash 中输入 winpty python server.py以启动本程序
# 然后再浏览器中键入localhost:8000来给服务器发送request
# 在网址后加'/'后可以添加request参数
