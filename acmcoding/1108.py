#encoding:utf8
##求最小公倍数

##先求最大公约数
def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)

#print gcd(18,10)

def Lowest_Common_Multiple(x,y):
    return x*y/gcd(x,y)

print Lowest_Common_Multiple(10,18)
