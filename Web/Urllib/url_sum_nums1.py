import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_164644.html'
html = urllib.request.urlopen(url, context=ctx).read()
# generate a bs4 object which parses the html content as a tree
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

Sum = 0
for tag in tags:
   Sum += int(tag.contents[0])
print(Sum)
