#encoding:utf8
#母牛的故事

##思路：这道题有点类似于Fibonacci数列，用递推关系来走，经过分析，其递推公式为：
##f1=1,f2=2,f3=3,f4=4,f(n)=n+f(n-4)

def cow_num(n):
    if n==0:
        return None

    else:
        if n in range(1,5):
            return n
        return n+cow_num(n-4)

print cow_num(2)
print cow_num(4)
print cow_num(5)
print cow_num(6)
print cow_num(0)
