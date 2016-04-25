#encoding:utf8
#18_2动态规划和0／1背包问题.py
import random
#17_1背包问题.py
#构建一组有序物品
class Item(object):
    def __init__(self,n,v,w):
        self.name=n
        self.value=float(v)
        self.weight=float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result='<'+self.name+','+str(self.value)+','+str(self.weight)+'>'
        return result
#使用决策树解决背包问题
#toConsider:上层节点（对应递归调用栈中之前的调用）中还没有被选择的物品
#avail:剩余的可用空间
def maxVal(toConsider,avail):
    '''假设toConsider是一个列表，avail是重量
       返回一个元组，包含0／1背包最优解的总重量和最优解包含的物品'''
    if toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getWeight()>avail:
        #只遍历右分支
        result=maxVal(toConsider[1:],avail)
    else:
        nextItem=toConsider[0]
        #遍历左分支
        withVal,withToTake=maxVal(toConsider[1:],avail-nextItem.getWeight())
        withVal+=nextItem.getValue()
        #遍历右分支
        withoutVal,withoutToTake=maxVal(toConsider[1:],avail)
        #选择更优的分支
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

def smallTest():
    names=['a','b','c','d']
    vals=[6,7,8,9]
    weights=[3,3,2,5]
    Items=[]
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    val,taken=maxVal(Items,5)
    for item in taken:
        print item
    print 'Total value of items taken=',val
# smallTest()

# #测试基于决策树的实现
# def buildManyItems(numItems,maxVal,maxWeight):
#     items=[]
#     for i in range(numItems):
#         items.append(Item(str(i),random.randint(1,maxVal),random.randint(1,maxWeight)))
#     return items
#
# def bigTest(numItems):
#     items=buildManyItems(numItems,10,10)
#     val,taken=maxVal(items,40)
#     print 'Items Taken'
#     for item in taken:
#         print item
#     print 'Total value of items taken=',val
# bigTest(10)

#背包问题的动态规划解法
def fastMaxVal(toConsider,avail,memo={}):
    '''假设toConsider是物品列表，avail是重量 ，memo只会用在递归调用中
       返回一个元组，包含／1背包最优解的总重量和最优解包含的物品'''
    if(len(toConsider),avail) in memo:
        result=memo[(len(toConsider),avail)]
    elif toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getWeight()>avail:
        #只遍历右分支
        result=fastMaxVal(toConsider[1:],avail,memo)
    else:
        nextItem=toConsider[0]
        #遍历左分支
        withVal,withToTake=fastMaxVal(toConsider[1:],avail=-nextItem.getWeight(),memo)#提示错误
        withVal+=nextItem.getValue()
        #遍历右分支
        withoutVal,withoutToTake=fastMaxVal(toConsider[1:],avail,memo)
        #选择更优的分支
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    memo[(len(toConsider),avail)]=result
    return result

#测试基于决策树的实现
def buildManyItems(numItems,maxVal,maxWeight):
    items=[]
    for i in range(numItems):
        items.append(Item(str(i),random.randint(1,maxVal),random.randint(1,maxWeight)))
    return items

def bigTest(numItems):
    items=buildManyItems(numItems,10,10)
    val,taken=fastMaxVal(items,40)
    print 'Items Taken'
    for item in taken:
        print item
    print 'Total value of items taken=',val
bigTest(10)
