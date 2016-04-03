#encoding:utf8
#1090 A+B for Input-Output Practice(II)

n=int(raw_input())
l=[]
lst=[]
for i in range(n):
    l.append(raw_input().split(' '))
    lst.append(map(int,l[i]))
for i in range(n):
    print sum(lst[i])
