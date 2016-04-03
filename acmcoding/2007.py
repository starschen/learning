#encoding:utf8
#2007平方和与立方和
#原习题的题目我不太能理解，测试例子中输入和输出的结果

def odd(x):
    return x%2!=0

def even(x):
    return x%2==0

def func(L):
    l_odd=filter(odd,L)
    #print l_odd
    l_even=filter(even,L)
    #print l_even

    sum_squ=0
    for i in l_even:
        sum_squ=sum_squ+i**2

    sum_cub=0
    for i in l_odd:
        sum_cub=sum_cub+i**3
    return sum_squ,sum_cub


print func([1,3,2,5])
print func([1,3,5,7])
print func([2,4,6,8])
