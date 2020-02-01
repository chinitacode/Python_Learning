'''
Passing Parameters In URLs
'''
import requests

# http get request
payload = {'key1': 'value1 ', 'key2': 'value2 '}
r1 = requests.get('https://httpbin.org/get', params=payload)
print(r1.url) # https://httpbin.org/get?key1=value1+&key2=value2+

# http post request:
payload = {'key1': 'value1 ', 'key2': ['value2', 'value3']}
r2 = requests.post('https://httpbin.org/post', params=payload)
print(r2.url) # https://httpbin.org/post?key1=value1+&key2=value2&key2=value3


'''
If we want to send some form-encoded data — much like an HTML form.
To do this, simply pass a dictionary to the data argument.
Our dictionary of data will automatically be form-encoded when the request is made:
'''
payload = {'key1': 'value1 ', 'key2': ['value2', 'value3']}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
'''
  "form": {
    "key1": "value1 ",
    "key2": [
      "value2",
      "value3"
    ]
  }, ...


The data argument can also have multiple values for each key.
This can be done by making data either a list of tuples or a dictionary with lists as values.
This is particularly useful when the form has multiple elements that use the same key:

'''
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
'''
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
'''

print(r1.text == r2.text) # True


'''
https://requests.readthedocs.io/en/master/user/quickstart/#passing-parameters-in-urls
'''
