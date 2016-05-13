# def selSort(l):
#     pre=0
#     while pre!=len(l):
#         for i in range(pre,len(l)):
#             if l[pre]>l[i]:
#                 l[pre],l[i]=l[i],l[pre]
#         pre+=1
#     print l
#
# l=[9,5,7,4,6,1,3]
# print selSort(l)

def compare(x,y):
    if x<=y:
        return True
    else:
        return False

def merge(leftList,rightList,compare):
    result=[]
    i,j=0,0
    while i<len(leftList) and j<len(rightList):
        if compare(leftList[i],rightList[j]):  #leftList[i]<=rightList[j] return True
            result.append(leftList[i])
            i+=1
        else:
            result.append(rightList[j])
            j+=1
    while i<len(leftList):
        result.append(leftList[i])
        i+=1
    while j<len(rightList):
        result.append(rightList[j])
        j+=1
    return result

# import operator
def mergeSort(l,compare):
    if len(l)<2:
        return l[:]
    else:
        middle=len(l)//2
        leftList=mergeSort(l[:middle],compare)
        rightList=mergeSort(l[middle:],compare)
        return merge(leftList,rightList,compare)

l1=[1,5,12,18,19,20]
l2=[2,3,4,17]
l3=[9,5,7,4,6,1,3]
# print merge(l1,l2,compare)
print mergeSort(l3,compare)
