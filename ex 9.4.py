fname = 'mbox-short.txt'
fh = open(fname)
counts = dict()
for line in fh:
    if line.startswith('From '):
        time = line.split()[5]
        hours = time.split(':')[0]
        counts[hours] = counts.get(hours, 0) + 1
lst = list()
for k,v in counts.items():
    lst.append((k, v))
lst.sort()
for k,v in lst:
    print(k, v)