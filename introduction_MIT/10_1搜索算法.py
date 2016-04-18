#encoding:utf8
#10.1搜索算法

#线性搜索和间接访问元素
def search(l,e):
    for i in range(len(l)):
        if l[i]==e:
            return True
    return False

#二分查找和利用假设
def search(l,e):
    for i in range(len(l)):
        if l[i]==e:
            return True
        if l[i]>e:
            return False
    return False

# print search([1,2,3],2)
# print search([3,2,1],2)

#递归二分查找
def search(l,e):
    def bsearch(l,e,low,high):
        if high==low:
            return l[low]==e
        mid=(low+high)//2
        if l[mid]==e:
            return True
        elif l[mid]>e:
            if low==mid:
                return False
            else:
                return bsearch(l,e,low,mid-1)
        else:
            return bsearch(l,e,mid+1,high)

    if len(l)==0:
        return False
    else:
        return bsearch(l,e,0,len(l)-1)

print search([1,2,3],2)
print search([4,5,6],2)
