'''
利用requests将HTTP cookies从一个请求传递到另一个
'''


# First request
resp1 = requests.get(url)
...

# Second requests with cookies received on first requests
resp2 = requests.get(url, cookies=resp1.cookies)
