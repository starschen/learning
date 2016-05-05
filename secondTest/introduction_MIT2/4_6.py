#encoding:utf8
nameHandle=open('kids','w')
for i in range(2):
    name=raw_input('Enter your name:')
    nameHandle.write(name+'\n')
nameHandle.close()

nameHandle=open('kids','r')
for line in nameHandle:
    print line
nameHandle.close()

nameHandle=open('kids','w')
nameHandle.write('lily\n')
nameHandle.write('lucy\n')
nameHandle.close()

nameHandle=open('kids','r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()
