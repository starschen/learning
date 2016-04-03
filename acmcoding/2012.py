#encoding:utf8
##2012素数判定

##1 是3.16写的，没有写完，当然也是错的，但是我还是留下来吧，以后再看看我写这乱七八糟的代码，哈哈！
from itertools import ifilter  #此处与上不同
##廖教程中素数判断
##埃氏筛法，就是说从2开始的所有自然数，先用2把序列中的2的倍数筛掉，得到新序列（3开始的奇数序列）
##然后，再将新序列中用3把序列中3的倍数筛掉，得到新序列，以此类推，筛掉5的倍数，筛掉7的倍数……最
##后筛下来的便是我们要求的素数序列

# def _odd_iter(): #构造了一个奇数序列生成器，此处特意构造的生成器主要是因为在下面引用时需要是生成器
#     n=1
#     while True:
#         n=n+2
#         yield n  #这是个生成器，是个无限的序列
#
# def _not_divisible(n): #定义了筛选函数，将素数筛选出来
#     return lambda x:x%n>0
#
# def primes(l):    #定义生成器，不断地返回下一个素数
#     yield 2      #此生成器的第一个元素是2
#     it=_odd_iter()  #这时的it是生成器
#     while True:     #这也是一个无限循环的序列
#         n=next(it)  #生成器指向序列下一个数
#         yield n
#         it=ifilter(_not_divisible(n),it)  #筛选出来素数
#         yield it
#
# ##已经被我搞得乱七八糟的了，这都是啥啊
# def is_prime(x,y):
#     if x==0 and y==0:
#         return None
#     else:
#         s=[]
#         for n in range(x,y+1):
#             s.append(n**2+n+41)


##2
#思路：构造一个判断素数函数，题目中的多项式中n取{x:y}会生成一个list
#将生成的list里的每个数做素数判断，若全是素数，返回‘ok’，若不全是素数，返回'no'，x=0y=0时结束
def func(n):
    return lambda x:x%n>0  #这是一个生成器

#在一定范围内找素数
def primes(x):
    l=(x for x in range(2,x+1))
    #yield 2             #加上这句的话在下面打印出来的2是单独一个list，其余的是一个list
    n=next(l)
    l=filter(func(n),l)
    yield l           #生成的是在（3，x）内的素数生成器,[如何把2也打印出来呢?]

def is_prime(x):
    for i in primes(x):
        return i     #将(3,x)内的素数生成列表
    if x in i:
        return True
    return False

# print is_prime(20)
# print is_prime(17)

def f(x,y):
    if x==0 and y==0:
        return None
    else:
        l=[]
        for n in range(x,y+1):
            s=n**2+n+41
            l.append(s)
        #print l
        lst=filter(is_prime,l)
        #print lst

        if len(lst)==len(l):
            print 'ok'
        else:
            print 'no'



f(1,5)
f(0,1)
f(0,0)










# is_prime(0,10)
# is_prime(0,0)
