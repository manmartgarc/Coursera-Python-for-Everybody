import urllib.request, urllib.parse, urllib.error
import json
import time

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
censusurl = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?'

def mapcheck(address):
    #address = '30 chapel st new haven'
    #time.sleep(3)
        #while True:
    if len(address) < 1:
        print('---- Program stopped by the user----')
        #break
    
    url = (censusurl + urllib.parse.urlencode({'address': address})
        + '&benchmark=Public_AR_Current' + '&format=json' )
    #print('----------------------------------------------')
    #print('Retrieving', url)
    try:
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
    except:
        time.sleep(3)
        try:
            uh = urllib.request.urlopen(url)
            data = uh.read().decode()
        except:
            time.sleep(3)
            try:
                uh = urllib.request.urlopen(url)
                data = uh.read().decode()
            except:
                pass
    #print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or js['result']['addressMatches'] == []:
        return str('address not found')
        pass
    elif js['result']['addressMatches'] != []:
        lat = js['result']['addressMatches'][0]['coordinates']['y']
        lng = js['result']['addressMatches'][0]['coordinates']['x']
        return (float(lat), float(lng))
    #return print((float(lat), float(lng)))
    #        print('----------------------------------------------')
    #        print('lat', lat, 'lng', lng)
    #        print('----------------------------------------------')
    #        location = js['results'][0]['formatted_address']
    #        print('----------------------------')
    #        print('Best fit: ', location)
    #        print("")
