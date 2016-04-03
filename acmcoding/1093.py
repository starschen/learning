#encoding:utf8
##1093 A+B for Input-Output Practice(V)

n=int(raw_input())
l=[]
for i in range(n):
    l.append(raw_input().split(' '))
    l[i]=map(int,l[i])

for i in range(n):
    print sum(l[i][1:])
