#encoding:utf8
##1018 big number

def factiorial(n):
    if n==1:
        return 1
    else:
        return n*factiorial(n-1)

n=int(raw_input())
s=[]
l=[]
for i in range(n):
    l.append(raw_input())
l=map(int,l)
for i in range(n):
    s.append(factiorial(l[i]))
    m=len(str(s[i]))
    print m
