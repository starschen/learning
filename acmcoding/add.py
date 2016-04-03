问题汇总

#1、矩阵相关
np.sum(l,axis=0,dtype=int) #axis＝0按列求和     2023
np.sum(l,axis=1,dtype=int) #axis＝0按行求和     2023
#for 循环中，a[i][j]按行循环i为行，j为列，按列循环就为a[j][i]     2025

#2 函数相关
ord()    #转ASCII值         2017
chr()    #ASCII值转               1048
round( ,n) #保留n位小数    2011
set()     #去重和排序 若想得到列表，需要 list(set())    2019
sorted( ,reverse=1)  #从大到小排序      2020
s.replace(a ,b )       #将b替换a       2025
str.index(str, beg=0, end=len(string))  #查找str的位置，从beg到end    2025
list.insert(index, obj)  #在index位置插入obj       2025
str.capitalize()        #要注意是对str首字母大写    2026
' '.join(s)    #将s中的元素以空格合并          2026
zip()      #压缩的函数，但是真心不会 2032




#3字典应用
dic.get(func,'否则') #对元素用func函数运算，得到的值存在于dic的key,则办理出相应的value,若没有则输出‘否则’   2004
dic[key]=value      #给字典赋值      2022


#4循环相关
##1 初始化不要放到循环里。   2005
##2 返回值不要在循环里返回，要跳出循环返回



#5类型相关
##1初始化定义时不能放在一起，如positive,negtive,zero=0是错误的。  2008




#6判断素数                               2012
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


#8numpy相关
import numpy as np
np.array(l,dtype=int)  #将l转化成整型的矩阵  2023
np.sum(l,axis=1,dtype=float)     #axis=1 按行求sum,结果返回float    2023
np.sum(l,axis=0,dtype=float)     #axis=0 按列求sum,结果返回float     2023


#9输入输出相关
'\''  #转义符
'\n'  #换行符
'\t'  #制表符
