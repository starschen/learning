#encoding:utf8
#2010水仙花数

#1
#穷举法实现判断一个数是否是水仙花数
def flower(x):
    if x>=100 and x<=999:
        a=x/100
        #print a
        b=x/10%10
        #print b
        c=x%100%10
        #print c
        if x==a**3+b**3+c**3:
            return True
        return False

def flower_num(n,m):
    l=list()
    for i in range(n,m+1):
        if flower(i):
            l.append(i)
    return l

print flower_num(100,120)
print flower_num(300,380)
print flower_num(90,99)

#2不限制一定是三位数 参考
def flower(num):
    s=str(num)
    if reduce(lambda sum,x:sum+int(x)**3,s,0)==num: #高手写法
        return True
    return False

def flower_num(n,m):
    l=filter(flower,range(n,m+1))
    if len(l)==0:
        print 'no'
    else:
        for i in l:
            print i,
        print

flower_num(100,120)
flower_num(300,380)
flower_num(90,99)
