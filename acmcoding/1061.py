#encoding:utf8
#1061 Rightmost Digit

def func(x):
    return x**x

n=int(raw_input())
l=[]
lst=[]
s=[]
for i in range(n):
    l.append(int(raw_input()))     #l=[3,4]
    lst.append(func(l[i]))

for i in range(n):
    s.append(str(lst[i]))         #将int改为string
    print s[i][-1]
