from urllib import request
import ssl, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving ', url)
data = request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

count = len(js['comments'])
print('count: ', count)

Sum = 0
for comment in js['comments']:
    Sum += int(comment['count'])
print('Sum: ',Sum)
