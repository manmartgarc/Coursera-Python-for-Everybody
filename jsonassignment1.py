import urllib.request, urllib.parse, urllib.error
import json

#test url http://py4e-data.dr-chuck.net/comments_42.json

while True:
    count = 0
    sum = 0
    url = input('Please enter the URL, otherwise press the return key to quit: ')
    if len(url) < 1:
        print('----Program stopped by user----')
        break
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Successfully retrieved', len(data), 'characters')
    info = json.loads(data)
    for comment in info['comments']:
        count = count + 1
        sum = sum + int(comment['count'])
    print('--------------------------------------')
    print('There are', count, 'comments')
    print('The sum of all the count values is', sum)
    print('--------------------------------------')