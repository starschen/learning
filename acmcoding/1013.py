#encoding:utf8
##1013 Digital Roots

n=int(raw_input())
l=[]
while (n!=0):
    l.append(n)
    n=int(raw_input())
# print l
for i in l:
    m=i%10
    # print 'm=',m
    n=i/10
    sum=m+n
    # print 'n=',n
    if sum<=10:
        print sum
    else:
        m=sum%10
        # print m
        n=sum/10
        # print n
        print m+n
