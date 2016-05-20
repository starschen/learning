#encoding:utf8
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

def greedy(items,maxWeight,keyFunction):
    itemsCopy=sorted(items,key=keyFunction,reverse=True)
    result=[]
    totalValue=0.0
    totalWeight=0.0
    for i in range(len(itemsCopy)):
        if(totalWeight+itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalValue+=itemsCopy[i].getValue()
            totalWeight+=itemsCopy[i].getWeight()
    return (result,totalValue)

def testGreedy(items,constraint,keyFunction):
    taken,val=greedy(items,constraint,keyFunction)
    print 'Total value of items taken=',val
    for item in taken:
        print '    ',item

def testGreedys(maxWeight=20):
    items=buildItems()
    print 'Use greedy by value to fill knapsack of size',maxWeight
    testGreedy(items,maxWeight,value)

    print '\nUse greedy by weight to fill knapsack of size',maxWeight
    testGreedy(items,maxWeight,weightInverse)

    print '\nUse greedy by density to fill knapsack of size',maxWeight
    testGreedy(items,maxWeight,density)

# testGreedys()

def getBinaryRep(n,numDigits):
    result=''
    while n>0:
        result=str(n%2)+result
        n=n//2
    if len(result)>numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits-len(result)):
        result='0'+result
    return result

def genPowerset(L):
    powerset=[]
    for i in range(2**len(L)):
        binStr=getBinaryRep(i,len(L))
        subset=[]
        for j in range(len(L)):
            if binStr[j]=='1':
                subset.append(L[j])
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
    pset=genPowerset(items)
    taken,val=chooseBest(pset,maxWeight,Item.getValue,Item.getWeight)
    print 'Total value of items taken=',val
    for item in taken:
        print item

testBest()
