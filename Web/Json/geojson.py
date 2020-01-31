import urllib.request, urllib.parse, urllib.error, json, ssl
api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    addr = input('Enter location: ')
    if len(addr) < 1: break

    parms = dict()
    parms['address'] = addr
    parms['key'] = api_key
    # Concatenate the url and the query
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print('Place id: ', js['results'][0]["place_id"])
