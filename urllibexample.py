import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for v,k in counts.items():
    lst.append((k,v))
lst.sort(reverse = True)
for v,k in lst:
    print(v,k)