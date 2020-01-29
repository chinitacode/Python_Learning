import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')# 'http://py4e-data.dr-chuck.net/known_by_Devlin.html'
count = int(input('Enter count: '))# 7
position = int(input('Enter position: '))# 18

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

names = []
print('Retrieving: %s' % url)
while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')[position - 1]
    url = tag.get('href', None)
    print('Retrieving: %s' % url)
    names.append(tag.contents[0])
    count -= 1

print(names[-1])

'''
Enter URL: http://py4e-data.dr-chuck.net/known_by_Devlin.html
Enter count: 7
Enter position: 18
Retrieving: http://py4e-data.dr-chuck.net/known_by_Devlin.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Narissa.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Kyren.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Ayah.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Jacqui.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mariette.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Saarah.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Hayleigh.html
Hayleigh
'''
