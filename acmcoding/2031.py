#encoding:utf8
##2031进制转换

##未解决：负数怎么转换3.24

##参考http://www.cnblogs.com/zhangpengshou/archive/2012/03/12/2392068.html
#base=[0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]

#r>=2 and r<=10
def dec2r(n,r):
    base=[str(x) for x in range(10)]+[chr(x) for x in range(ord('A'),ord('A')+6)]
    a=[]
    if r>=2 and r<=10:
        while n/r!=0:
            a.append(n%r)
            n=n/r
        a.append(n%r)
        #print a
        return ''.join([str(x) for x in a[::-1]])

    elif r>10 and r<=16:
        base=base[:r]
        while n/r!=0:
            a.append(base[n%r])
            n=n/r
        a.append(base[n%r])
        return ''.join([str(x) for x in a[::-1]])
        #print a


print dec2r(9,2)
print dec2r(25,8)
print dec2r(23,12)
print dec2r(-4,3)
