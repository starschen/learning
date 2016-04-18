#encoding:utf8
#10.2排序算法

#选择排序 原书代码有点问题，这一段是自己写的
def selsort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l

# print selsort([2,5,8,6,3,7])

#归并排序
def merge(left,right,compare):
    '''left 和right是两个有序列表，返回两个列表组成的新有序列表'''
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

import operator
def mergesort(l,compare=operator.lt):
    '''l列表，compare定义了元素的顺序，返回一个排序后的列表'''
    if len(l)<2:
        return l[:]
    else:
        middle=len(l)//2
        left=mergesort(l[:middle],compare)
        right=mergesort(l[middle:],compare)
        return merge(left,right,compare)


# print mergesort([2,5,8,6,3,7])

#把函数当做参数 排序人名列表
import string
def lastnamefirstname(name1,name2):
    name1=name1.split(' ')
    name2=name2.split(' ')
    if name1[1]!=name2[1]:
        return name1[1]<name2[1]
    else:
        return name1[0]<name2[0]

def fistnamelastname(name1,name2):
    name1=name1.split(' ')
    name2=name2.split(' ')
    if name1[0]!=name2[0]:
        return name1[0]<name2[0]
    else:
        return name1[1]<name2[1]

# l=['Chris Terman','Tom Brady','Eric Grimson','Gisele Bundchen']
# new1=mergesort(l,lastnamefirstname)
# print 'sorted by last name=',new1
# new2=mergesort(l,fistnamelastname)
# print 'sorted by first name=',new2

# l=[3,5,2]
# d={'a':12,'c':5,'b':'dog'}
# print sorted(l)
# print l
# l.sort()
# print l
# print sorted(d)
# d.sort()    #error:dict object has no attribute 'sort'

l=[[1,2,3],(3,2,1,0),'abc']
print sorted(l,key=len,reverse=True)
