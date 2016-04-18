#encoding:utf8
#9.1思考计算复杂度

def f(i):
    """假定type(i)是整数，并且i>=0"""
    answer=1
    while i>=1:
        answer*=i
        i-=1
    return answer

def linearsearch(l,x):
    for e in l:
        if e ==x:
            return True
        return  False

def fact(n):
    '''if n is int,return n!'''
    answer=1
    while n>1:
        answer*=n
        n-=1
    return answer

#穷举法寻找近似平方根
def squarerootexhaustive(x,epsilon):
    '''assume x and epsilon are float and epsilon<1
       if exist y and the distant of y*yand x less than epsilon,return y'''
    step=epsilon**2
    ans=0.0
    while abs(ans**2-x)>=epsilon and ans*ans<=x:
        ans+=step
    if ans*ans>x:
        raise ValueError
    return ans

#二分查寻找近似平方根
def squarerootbi(x,epsilon):
    '''assume x and epsilon are float and epsilon<1
       if exist y and the distant of y*yand x less than epsilon,return y'''
    low=0.0
    high=max(1.0,x)
    ans=(high+low)/2.0
    while abs(ans**2-x)>=epsilon:
        if ans**2<x:
            low=ans
        else:
            high=ans
        ans=(high+low)/2.0
    return ans
