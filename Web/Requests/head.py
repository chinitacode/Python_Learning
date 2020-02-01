'''
用 requests 库发起一个HEAD请求，并从响应中提取出一些HTTP头数据的字段
'''

import requests

resp = requests.head('http://www.python.org/index.html')

status = resp.status_code
last_modified = resp.headers['last-modified']
content_type = resp.headers['content-type']
content_length = resp.headers['content-length']
