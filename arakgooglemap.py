import urllib.request, urllib.parse, urllib.error
import json
import csv

fh = open('address.csv')
reader = csv.reader(fh)
addresses = list()
for row in reader:
    addresses.append(row[0])
addresses.remove(addresses[0])

addfix = list()
for i in range(3):
    addfix.append([])

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
for address in addresses:
    #address = input('Please enter address,\notherwise please press return to exit the program: ')
    if len(address) < 1:
        print('---- Program stopped by the user----')
        break
    
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('----------------------------------------------')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
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
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('----------------------------------------------')
    print('lat', lat, 'lng', lng)
    print('----------------------------------------------')
    location = js['results'][0]['formatted_address']
    print('----------------------------')
    print('Best fit: ', location)
    print("")
    addfix[0].append(lat)
    addfix[1].append(lng)
    addfix[2].append(location)