import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter location: ') #http://py4e-data.dr-chuck.net/comments_42.xml
print('Retrieving %s' % location)
data = urllib.request.urlopen(location, context=ctx).read().decode()
print('Retrieved %s characters' % (len(data)))
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count: %s' % (len(counts)))
Sum = 0
for count in counts:
    Sum += int(count.text)
print('Sum: %s' % Sum)
