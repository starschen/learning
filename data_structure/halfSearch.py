#encoding:utf8
#有序折半查找

def halfSearch(lst,e):
    low=0
    high=len(lst)-1
    while low<high:
        half=(low+high)/2
        if e>lst[half]:
            low=half+1
        elif e<lst[half]:
            high=half-1
        else:
            return half
    return None

l=[2,4,6,7,8,10,22,45]
print halfSearch(l,10)
