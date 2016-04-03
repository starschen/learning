#encoding:utf8
#数据的交换输出

##思路：先找到最小的数，再做替换

def find_min(l):
    min=l[1]
    for i in range(1,len(l)):
        if min>=l[i]:
            min=i
    return min
#print find_min([4,2,1,3,4])


def change(l):
    if l[0]==0:
        return None
    else:
        temp=l[find_min(l)]
        # print temp
        l[find_min(l)]=l[1]
        # print l[find_min(l)]
        l[1]=temp
        # print l[1]
        print l[1:]

change([4,2,1,3,4])
change([5,5,4,3,2,1])
change([0])
