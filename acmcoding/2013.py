#encoding:utf8
#蟠桃记

##思路：这道题分析起来应该是递归，表达成递归公式应该是:a(1)=x,a(n-1)=1/2*a(n-2)-1,a(n)=1，给定n值，求x
##原题意是依次递减的数列，根据我个人习惯将其改成递增数列：b(1)=1,b(n)=2(b(n-1)+1),给定n，求b(n)

def func(n):
    if n==1:
        return 1
    return 2*func(n-1)+2


print func(2)
print func(4)
