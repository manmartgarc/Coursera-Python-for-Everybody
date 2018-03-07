import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

for i in range(0, count):
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[(pos-1)].get('href', None)
    url = tag
print("")
print(re.findall('known_by_(.+)\.', tag))