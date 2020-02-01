'''
如果需要在发出的请求中提供一些自定义的HTTP头，例如修改 user-agent 字段,
可以创建一个包含字段值的字典，并创建一个Request实例然后将其传给urlopen()。
'''

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

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}

req = request.Request(base_url, query_string.encode(), headers=headers)

# Make a request and read the response
response = request.urlopen(req).read().decode()

print(response)
