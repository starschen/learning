#encoding:utf8
#2035 人见人爱A^B

#输出存在点问题4.6
def func(a,b):
    return a**b

l=raw_input().split(' ')
s=[]
lst=[]
while( l!=['0','0']):
    s.append(l)
    l=raw_input().split(' ')
    for i in s:
        i=map(int,i)
        m=func(i[0],i[1])
        m=str(m)
        print m[-3:]
