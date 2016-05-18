#encoding:utf8

def quickSort(l,low,high): #对l进行快速排序
    if low<high:
        q=partSort(l,low,high)
        quickSort(l,low,q-1)
        quickSort(l,q+1,high)
    return l

def partSort(l,low,high):
    i=low
    j=high
    key=l[i]
    while i<j:
        while i<j and l[j]<key:
            l[i]=l[j]
            i+=1
            l[j]=l[i]
        while i<j and l[j]>=key:
            j-=1
    l[i]=key
    return i


l=[9,5,7,4,6,1,3]
print quickSort(l,0,len(l)-1)
