import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#URL = http://py4e-data.dr-chuck.net/comments_42.xml


URL = input('Enter URL: ')
uhand = urllib.request.urlopen(URL)
print('Retrieving:', URL)
data = uhand.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst = (tree.findall('comments/comment'))
print('Count of counts is', len(lst))
countlst = list()
for count in lst:
    countlst.append(int(count.find('count').text))
print('Sum of counts is', sum(countlst))

