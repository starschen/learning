#encoding:utf8
#2_9线性时间选择.py
import random
def partition(l,p,r):
    i=p
    j=r
    key=l[p]
    while i<j:
        while i<j and l[j]<=key:
            l[i]=l[j]
            i+=1
            l[j]=l[i]
        while i<j and l[j]>key:
            j-=1
    l[i]=key
    return i

def randomizedParitition(l,p,r):
    i=random.randrange(p,r-1,1)
    l[i],l[p]=l[p],l[i]
    return partition(l,p,r)

def randomQuickSort(l,p,r):
    q=randomizedParitition(l,p,r)
    randomQuickSort(l,p,q-1)
    randomQuickSort(l,q+1,r)
    return l

l=[9,5,7,4,6,1,3]
# print randomQuickSort(l,0,len(l)-1)
# print randomizedParitition(l,0,len(l)-1)
print partition(l,0,len(l)-1)
