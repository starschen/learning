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
# print Ackerman(4,2)

#例2－4 排列问题
def swap(a,b):
    a,b=b,a
    return a,b

def Perm(l,k,m):
    '''设R={r1,r2,...,rn}是要进行排列的n个元素,Ri=R-{ri}.集合X中元素的全排列记为Perm(X).
    (ri)Perm(X)表示在全排列Perm(X)的每一个排列前加上前缀ri得到的排列。R的全排列归纳定义如下：
    当n=1,Perm(R)=(r),其中r是集合R中唯一的元素
    当n>1,Perm(R)由(r1)Perm(R1),(r2)Perm(R2),...,(rn)Perm(Rn)构成'''
    if k==m:
        return l
    else:
        for i in range(k,m+1):
            swap(l[k],l[i])
            Perm(l,k+1,m)
            swap(l[k],l[i])

#例2－5 整数划分问题
def intDiv(n,m):
    '''将正整数n表示成一系列正整数的和，n=m1+m2+...+mi; （其中mi为正整数，并且1 <= mi <= n），
       则{m1,m2,...,mi}为n的一个划分。如果{m1,m2,...,mi}中的最大值不超过m，即max(m1,m2,...,mi)<=m，
       则称它属于n的一个m划分。这里我们记n的m划分的个数为intDiv(n,m)'''
    if n==1 or m==1:
        return 1
    elif n<m:
        return intDiv(n,n)
    elif n==m:
        return (1+intDiv(n,m-1))
    else:
        return intDiv(n-m,m)+intDiv(n,m-1)

# print intDiv(6,6)

#例2－6 Hanoi塔问题
#在网上看到的例子，来源不详，若有侵权请告知立刻删除
steps=0
def move(n,A,B):
    global steps
    steps+=1
    print 'Move',n,'from',A,'to',B

def Hanoi(n,A,B,C):
    if n==1:
        move(n,A,B)
    else:
        Hanoi(n-1,A,C,B)
        move(n,A,B)
        Hanoi(n-1,C,B,A)

Hanoi(4,'A','B','C')
print 'steps=',steps
