# hand=open('mbox-short.txt')
# for line in hand:
#     line=line.rstrip()
#     if line.find('From')>=0:
#         print line


# import re
# hand=open('mbox-short.txt')
# for line in hand:
#     line=line.rstrip()
#     if re.search('From',line):
#         print line
#
# hand=open('mbox-short.txt')
# for line in hand:
#     lind=lind.rstrip()
#     if line.startswith('From:'):
#         print line
#
#
# import re
# hand=open('mbox-short.txt')
# for line in hand:
#     line=line.rstrip()
#     if re.search('^From:',line):
#         print line


import re
# x='My 2 favorite numbers are 19 and 42'
# y=re.findall('[0-9]+',x)
# print y
# y=re.findall('[AEIOU]+',x)
# print y

x='From: Using the :character'
y=re.findall('^F.+:',x)
print y
