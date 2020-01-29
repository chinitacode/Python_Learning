import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url here: ')  # http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url, context=ctx).read()
# generate a bs4 object which parses the html content as a tree
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags:
tags = soup('a')
# tag is a bs4.element.Tag object, likes a dictionary
for tag in tags:
    print(tag.get('href', None))
