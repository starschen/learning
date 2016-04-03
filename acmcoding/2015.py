#encoding:utf8
#偶数求和

##思路：先是构造偶数列，然后n%m得到该做几次每m个数求值,n/m得到最后不足m的有几个
##写法2回头认真看看，我感觉自己写的好啰嗦啊，一般人看不懂呢
##1
def sum_even(n,m):
    lst=range(2,(2*n+2),2)
    #print lst
    x=n%m
    y=n/m
    #print x,y
    s=[]
    if x==0:
        for i in range(1,y+1):
            s.append(sum(lst[((i-1)*m):i*m])/m)
        #print s
    else:
        for i in range(1,x+1):
            for j in range(1,i+1):
                s.append(sum(lst[(j-1):(j*m)])/m)
        #print s
        s1=sum(lst[(len(lst)-y):])/y
        #print s1
        s.append(s1)
    return s

print sum_even(3,2)
print sum_even(4,2)

##2 大鲍写的
def average(l):
    return sum(l)/len(l)

def sum_even(n,m):
    start=2
    current_num=start

    while n>m:
        l=range(current_num,current_num+2*m-1,2)
        print average(l),
        n=n-m
        current_num+=2*m

    if n>0:
        l=range(current_num,current_num+2*n-1,2)
        print average(l),
    print

sum_even(3,2)
sum_even(4,2)
