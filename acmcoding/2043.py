#encoding:utf8
##2043密码

n=int(raw_input())
l=[]
s=[]
for i in range(n):
    s.append(raw_input())
for i in range(len(s)):
    l.append(map(ord,s[i]))
for k in l:
    flag=[]
    if len(k)>=8 and len(k)<=16:
        for i in k:
            if i in range(65,91):
                flag.append('A')
            elif i in range(97,123):
                flag.append('a')
            elif i in range(48,58):
                flag.append('0')
            elif i in (33,51,52,53,58,64,94,126):
                flag.append(':')
            else:
                print 'NO'
        if len(set(flag))>=3:
            print 'YES'
        else:
            print 'NO'
    else:
        print 'NO'

# l='a1b2c3d4'
# l=map(ord,l)
