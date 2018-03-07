import re
#print( sum( [int(n) for n in re.findall('[0-9]+', open('C:/Users/billi/Google Drive/Python/Coursera/Intro/regex_sum_36763.txt').read()) ] ) )
numbers = list()
for n in re.findall('[0-9]+', open('C:/Users/billi/Google Drive/Python/Coursera/Intro/regex_sum_36763.txt').read()):
    numbers.append(int(n))
print(sum(numbers))    
    

