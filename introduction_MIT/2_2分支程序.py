#encoding:utf8
#2_2分支程序.py
#动手练习：编写一个程序，处理三个变量x，y，z，然后输出它们当中最大的奇数，如果其中没有奇数，输出一条信息说明

def isodd(a):
    if a%2==1:
        return True
    else:
        return False

def maxodd(x,y,z):
    oddlist=filter(isodd,[x,y,z])
    if len(oddlist)>0:
        print max(oddlist)
    else:
        print 'There are no odd numbers.'


maxodd(3,5,6)
maxodd(2,4,6)
maxodd(3,5,7)
