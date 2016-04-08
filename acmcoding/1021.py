#encoding:utf8
#1021 Fibonacci Again

def Fib(n):
    if n==0:
        return 7
    elif n==1:
        return 11
    else:
        return Fib(n-1)+Fib(n-2)

while True:
    n=int(raw_input())
    m=Fib(n)
    if m%3==0:
        print 'Yes'
    else:
        print 'No'
