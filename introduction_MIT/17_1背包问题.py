#encoding:utf8
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

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def buildItems():
    names=['clock','painting','radio','vase','book','computer']
    vals=[175,90,20,50,10,200]
    weights=[10,9,4,2,1,20]
    Items=[]
    for i in range(len(vals)):
        Items.append(Item(names[i],vals[i],weights[i]))
    return Items

#使用贪婪算法选择物品
def greedy(items,maxWeight,keyFunction):
    '''假设Items是列表， maxWeight>=0,那么keyFunction将Items的元素映射为float类型'''
    itemsCopy=sorted(items,key=keyFunction,reverse=True)
    result=[]
    totalValue=0.0
    totalWeight=0.0
    for i in range(len(itemsCopy)):
        if (totalWeight+itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalWeight+=itemsCopy[i].getWeight()
            totalValue+=itemsCopy[i].getValue()
    return (result,totalValue)

def testGreedy(items,constraint,keyFunction):
    taken,val=greedy(items,constraint,keyFunction)
    print 'Total value of items taken=',val
    for item in taken:
        print '   ',item

def testGreedys(maxWeight=20):
    items=buildItems()
    print 'Use greedy by value to fill knapsack of size',maxWeight
    testGreedy(items,maxWeight,value)
    print '\nUse greedy by weight to fill knapsack of size',maxWeight
    testGreedy(items,maxWeight,weightInverse)
    print '\nUse greedy by density to fill knapsack of size',maxWeight
    testGreedy(items,maxWeight,density)

# testGreedys()
#0／1背包问题的暴力最优解

#9.3生成超级集合
#指数复杂度
def getbinaryrep(n,numdigits):
    result=''
    while n>0:
        result=str(n%2)+result
        n=n//2
    if len(result)>numdigits:
        raise ValueError('not enough digits')
    for i in range(numdigits-len(result)):
        result='0'+result
    return result

def genpowerset(l):
    powerset=[]
    for i in range(2**len(l)):
        binstr=getbinaryrep(i,len(l))
        subset=[]
        for j in range(len(l)):
            if binstr[j]=='1':
                subset.append(l[j])
        powerset.append(subset)
    return powerset

def chooseBest(pset,maxWeight,getVal,getWeight):
    bestVal=0.0
    bestSet=None
    for items in pset:
        itemsVal=0.0
        itemsWeight=0.0
        for item in items:
            itemsVal+=getVal(item)
            itemsWeight+=getWeight(item)
        if itemsWeight<=maxWeight and itemsVal>bestVal:
            bestVal=itemsVal
            bestSet=items
    return (bestSet,bestVal)

def testBest(maxWeight=20):
    items=buildItems()
    pset=genpowerset(items)
    taken,val=chooseBest(pset,maxWeight,Item.getValue,Item.getWeight)
    print 'Total value of items taken=',val
    for item in taken:
        print item

testBest()
