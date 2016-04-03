#encoding:utf8
#2008数值统计
#思考：如果从列表中筛选出大于0的计数，或是形成新列表统计其长度？

#1
def num_statistic(L):
    positive=0    #之前犯了个错误，想要positive,negtive,zero=0统一定义，结果一直报错，这种还是不能列为一式定义
    negtive=0
    zero=0
    for i in L[1:]:
        if i>0:
            positive=positive+1
        elif i==0:
            zero=zero+1
        else:
            negtive=negtive+1
    return negtive,zero,positive

print num_statistic([5,-1,2,3,-2,4])
print num_statistic([5,-1,-2,-3,-4,-5])
print num_statistic([4,1,2,3,4,])
print num_statistic([4,1,2,3,0])
print num_statistic([4,-1,-2,-3,0])

#2
