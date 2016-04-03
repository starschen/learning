#encoding:utf8
##亲和数

def divisor(x):
    d=[]
    for i in range(1,x):
        if x%i==0:
            d.append(i)
    return d

def is_intimate(a,b):
    sum_a=sum(divisor(int(a)))
    sum_b=sum(divisor(int(b)))
    if sum_a==int(b) and sum_b==int(a):
        print 'YES'
    else:
        print 'NO'

m=int(raw_input())
l=[]
for i in range(m):
    l.append(raw_input().split(' '))

for i in range(m):
    is_intimate(l[i][0],l[i][1])
