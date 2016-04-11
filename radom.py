#encoding:utf8
#生成随机数

import random

def random_num(x,y,n):      #范围在(x,y)内随机产生n个随机数
    l=[]
    for i in range(n):
        m=random.uniform(x,y)
        l.append(m)
    return x,'to',y,'',n,'radom numbers are:',sorted(l)

# f=open('radom3.txt','w')
#
# print >>f,random_num(0,6,120)
# print >>f,random_num(6,35,65)
# print >>f,random_num(35,94,120)
# print >>f,random_num(94,117,65)
# f.close
#
#
# f=open('radom4.txt','w')
#
# print >>f,random_num(0,21,120)
# print >>f,random_num(21,32,65)
# print >>f,random_num(32,53,120)
# print >>f,random_num(53,64,65)
# f.close


f=open('radom5.txt','w')

print >>f,random_num(1,6,150)
print >>f,random_num(53,58,150)
print >>f,random_num(32,37,130)
f.close
