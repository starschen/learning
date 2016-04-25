#encoding:utf8
#18_1斐波那契数列.py
#斐波那契数列的递归实现
def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# print fib(120)

#带memo的斐波那契数列实现
def fastFib(n,memo={}):
    '''假设n>=0，memo只在递归调用中使用，返回n的斐波那契数列'''
    if n==0 or n==1:
        return 1
    try:
        return memo[0]
    except KeyError:
        result=fastFib(n-1,memo)+fastFib(n-2,memo)
        memo[n]=result
        return result

# print fastFib(120)
