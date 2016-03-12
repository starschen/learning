#encoding:utf8
def my_abs(x):
    if not isinstance(x,(int,float)):
        return TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

def enroll(name,gender,age=6,city='Beijing'):
    print 'name',name
    print 'gender',gender
    print 'age',age
    print 'city',city

def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

def person(name,age,**kw):
    print 'name:',name,'age:',age,'other:',kw

def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)