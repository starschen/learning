#encoding:utf8
#2_7合并排序.py

def compare(a,b):
    if a<=b:
        return True
    else:
        return False

def Merge(leftList,rightList):
    i,j=0,0
    sortedList=[]
    while i<len(leftList) and j<len(rightList):
        if compare(leftList[i],rightList[j]):
            sortedList.append(leftList[i])
            i+=1
        else:
            sortedList.append(rightList[j])
            j+=1
    while i<len(leftList):
        sortedList.append(leftList[i])
        i+=1
    while j<len(rightList):
        sortedList.append(rightList[j])
        j+=1
    return sortedList

def MergeSort(l):
    if len(l)<2:
        return l[:]
    else:
        mid=len(l)//2
        leftList=MergeSort(l[:mid])
        rightList=MergeSort(l[mid:])
        return Merge(leftList,rightList)

l3=[9,5,7,4,6,1,3]
print MergeSort(l3)
# l1=[1,5,12,18,19,20]
# l2=[2,3,4,17]
# print Merge(l1,l2)
