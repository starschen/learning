#encoding:utf8
##2001计算两点间的距离

import math
def distance((x1,y1),(x2,y2)):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

print distance((2,3),(5,7))
