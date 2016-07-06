import re
# hand=open('regex_sum_42.txt')
hand=open('regex_sum_272163.txt')
s=hand.read()
stuff=re.findall('[0-9]+',s)


print sum(map(int,stuff))
