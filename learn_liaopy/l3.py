#encoding:utf8

##1
def my_abs(x):
    if not isinstance(x,(int,float)):
        return TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

##2
import math

def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

##3
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

##4
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
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    else:
        return fact_iter(num-1,num*product)

