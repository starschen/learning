#encoding:utf8
#1003 Max Sum

t=int(raw_input())
s=[]
lst=[]
for i in range(t):
    s.append(raw_input().split(' '))
    s[i]=map(int,s[i])
# print s
for l in s:
    maxnum=l[0]
    for i in range(1,len(l)):
        for j in range(1,len(l)):
            # m=sum(l[i:j+1])
            #print m
            if maxnum<=sum(l[i:j+1]) and i!=j:
                maxnum=sum(l[i:j+1])
                x=i
                y=j
    print 'Case',i
    print maxnum,x,y
    print ''
