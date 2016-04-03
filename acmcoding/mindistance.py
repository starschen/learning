##输入：n个点的坐标
##输出：找到m个点，使得其它点距离m个点中的距离其最近的一点距离小于某值，输出这m个点，并输出其距离关系

#encoding:utf8

#输入l=[(x1,y1),(,),()]
import math

def distance((x1,y1),(x2,y2)):                    #求两点距离
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

##求出所有两点间的
