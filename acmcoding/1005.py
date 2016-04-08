#encoding:utf8
#1005 Number Sequence

def f(A,B,n):
    def func(n):
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            return (A*func(n-1)+B*func(n-2))%7
    return func(n)


l=raw_input().split(' ')
s=[]
while l!=['0','0','0']:
    s.append(l)
    l=raw_input().split(' ')
    for i in s:
        i=map(int,i)
        print f(i[0],i[1],i[2])

# print f(1,1,3)
# print f(1,2,10)
