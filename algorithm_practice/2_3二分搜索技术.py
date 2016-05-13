#encoding:utf8
#2_3二分搜索技术.py

def BinarySearch(l,e):
    '''在有序的列表l中，用二分搜索技术查找e，找到返回True'''
    low=0
    high=len(l)
    while low<=high-1:
        middle=(low+high)/2
        if l[middle]==e:
            print e,'located ',middle,' in l'
            return True
        elif l[middle]>e:
            high=middle-1
        else:
            low=middle+1
    return False

l=[1,2,3,4,5,6,7]
print BinarySearch(l,9)
print BinarySearch(l,7)
print BinarySearch(l,0)
