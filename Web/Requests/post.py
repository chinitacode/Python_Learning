'''
用requests库重新实现了http post请求
'''
import requests

# Base URL being accessed
base_url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

resp = requests.post(base_url, data=parms, headers=headers)

# Decoded text returned by the request
print(resp.text, '\n')
print(resp.content,'\n')
print(resp.json())


'''
resp.text 带给我们的是以Unicode解码的响应文本。
但如果去访问 resp.content ，就会得到原始的二进制数据;
如果访问 resp.json ，那么就会得到JSON格式的响应内容。
'''
