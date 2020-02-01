#发送一个简单的HTTP GET请求到远程的服务上

from urllib import request, parse

# Base URL being accessed
base_url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Encode the query string
query_string = parse.urlencode(parms)

# Make a GET request and read the response
response = request.urlopen(base_url + '?' + query_string).read().decode()

print(response)
