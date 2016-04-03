#encoding:utf8
##2042不容易系列之二


def func(N):
    if N==0:
        return 3
    else:
        return 2*(func(N-1)-1)


n=int(raw_input())
l=[]
for i in range(n):
    a=raw_input()
    l.append(a)
l=map(int,l)
print l


for i in l:
    print func(i)
