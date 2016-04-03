#encoding:utf8

##2002计算球体积

import math
def ballvolum(r):
    while r>=0:
        return 4.0/3*math.pi*r**3

print ballvolum(1)
print ballvolum(1.5)
