#encoding:utf8
#2_10最接近点对问题.py
#一维
def cpairl(l):
    while len(l)>1:
        mid=len(l)//2
        s1=l[:mid]
        print s1
        s2=l[mid:]
        print s2
        d1=cpairl(s1)
        print d1
        d2=cpairl(s2)
        print d2
    d=min(d1,d2,min(s2)-max(s1))
    return d

l=[1,4,6,10,11,15,18,20,30]
print len(l)
print cpairl(l)
