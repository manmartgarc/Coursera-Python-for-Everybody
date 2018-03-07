# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
flt_tot = 0
for lx in fh:
    if not lx.startswith("X-DSPAM-Confidence:"): 
        continue
    ipos = lx.find(':')
    flt = float(lx[ipos + 1: ])
    flt_tot = flt_tot + flt
    count = count + 1

print('Average spam confidence:', flt_tot/count)

