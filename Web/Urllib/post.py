# 如果需要使用POST方法在请求主体中发送查询参数，可以将参数编码后作为可选参数提供给 urlopen() 函数

from urllib import request, parse

# Base URL being accessed
base_url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
query_string = parse.urlencode(parms)

# Make a POST request and read the response
response = request.urlopen(base_url, query_string.encode()).read().decode()  # 或者encode('ascii')

print(response)
