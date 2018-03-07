import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
#test address South Federal University

while True:
    address = input('Please enter location, otherwise press the return key to quit: ')
    if len(address) < 1:
        print('----Program stopped by user----')
        break    
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
    if js['status'] != 'OK':
        print('Please enter a valid location.')
        continue    
    print('place_id for', address, 'is', js['results'][0]['place_id'])
        