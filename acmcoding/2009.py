#encoding:utf8
#2009求数列的和
#这道题想了半天怎么构造数列，唉，水平太不行啊，之前学的教程里明明就有教。还是不能做到灵活运用。
import math

##1用生成器生成数列
# def sqrt_iter(n,m):
#     ai=n
#     while m>0:          #生成器这还是用不太好
#         yield ai
#         ai=math.sqrt(ai)
#         m=m-1
#
# def seq_sum(n,m):
#     seq=list(sqrt_iter(n,m))
#     sum=0
#     for i in seq:
#         sum=sum+i
#     return round(sum,2)

##2用递归生成数列
def sqrt_iter(n,m):
    ai=n
    l=[n]
    for i in range(1,m):
        ai=math.sqrt(ai)
        l.append(ai)
    return l
print sqrt_iter(81,4)

def seq_sum(n,m):
    return round(sum(sqrt_iter(n,m)),2)

print seq_sum(81,4)
print seq_sum(2,2)
