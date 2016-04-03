#encoding:utf8

##1
l=[]
n=1
while n<=99:
    l.append(n)
    n=n+2

##2
def filb(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1