'''
If you’d like to add HTTP headers to a request, simply pass in a dict to the headers parameter.

For example, we didn’t specify our user-agent in the previous example:

>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}

>>> r = requests.get(url, headers=headers)
'''
