#encoding:utf8
##1092 A+B for Input-Output Practice(IV)

#这道题如果用python做，第一个输入值是可以忽略的，不用其也可以运行，但是第一个数可以用来做判断
l=map(int,raw_input().split(' '))
s=[]
if (len(l)!=l[0]+1):    
    print 'input Error'
else:
    while (l!=[0]):   #这部分需要加括号，要不0不返回
        s.append(l)
        l=map(int,raw_input().split(' '))
for i in range(len(s)):
    print sum(s[i][1:])
