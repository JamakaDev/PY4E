import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
endpoint = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input("Enter a place to search: ")
    if len(address) < 1: break


    parameters = dict()
    parameters['address'] = address
    parameters['key'] = api_key
    url = endpoint + urllib.parse.urlencode(parameters)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue


    print(js['results'][0]['place_id'])

