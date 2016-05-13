#encoding:utf8
#2_1递归的概念.py

#例2－1 阶乘函数
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

#例2－2 Fibonacci数列
def Fibonacci(n):
    if n==1 or n==2:
        return n
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

#例2－3 Ackerman函数
def Ackerman(n,m):
    if n==1 and m==0:
        return 2
    elif n==0:
        return 1
    elif m==0:
        return n+2
    else:
        return Ackerman(Ackerman(n-1,m),m-1)
print Ackerman(4,2)

#例2－4 排列问题
def Perm(l,k,m):
    '''设R={r1,r2,...,rn}是要进行排列的n个元素,Ri=R-{ri}.集合X中元素的全排列记为Perm(X).
    (ri)Perm(X)表示在全排列Perm(X)的每一个排列前加上前缀ri得到的排列。R的全排列归纳定义如下：
    当n=1,Perm(R)=(r),其中r是集合R中唯一的元素
    当n>1,Perm(R)由(r1)Perm(R1),(r2)Perm(R2),...,(rn)Perm(Rn)构成'''
    if k==m:
        for i in range(m):

#例2－5 整数划分问题
#例2－6 Hanoi塔问题
