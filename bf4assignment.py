import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all the span tags, take the contents and perform count and sum.
count = 0
sum = 0
tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    sum = sum + num
    count = count + 1
    print(count, '-', int(tag.contents[0]))
print("")
print('Count:', count)
print('Sum:', sum)