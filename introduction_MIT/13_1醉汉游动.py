#encoding:utf8
#13.1醉汉游动
import random
#Location类
class Location(object):

    def __init__(self,x,y):
        '''x和y是浮点数'''
        self.x=x
        self.y=y

    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self,other):
        ox=other.x
        oy=other.y
        xDist=self.x-ox
        yDist=self.y-oy
        return (xDist**2+yDist**2)**0.5

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'

#Field类
class Field(object):

    def __init__(self):
        self.drunks={}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk]=loc

    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist,yDist=drunk.takeStep()
        currentLocation=self.drunks[drunk]
        #使用Location的move方法来移动到新位置
        self.drunks[drunk]=currentLocation.move(xDist,yDist)

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

#Drunk基类
class Drunk(object):
    def __init__(self,name=None):
        '''name is char'''
        self.name=name

    def __str__(self):
        if self!=None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

#有bug的醉汉游动
def walk(f,d,numSteps):
    '''假定f是 Field， d是 f上的一个 Drunk， numSteps是正整数 ，d移动了 numSteps次，返回最终位置和起始位置的距离'''
    start=f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps,numTrials,dClass):
    '''假定numSteps 和numTrials是正整数， dClass是 Drunk的子类， 模拟numTrials次实验，每次 numSteps
       返回一个列表，包含每次实验的最终距离'''
    Homer=dClass()
    origin=Location(0.0,0.0)
    distances=[]
    for t in range(numTrials):
        f=Field()
        f.addDrunk(Homer,origin)
        distances.append(walk(f,Homer,numSteps))
    return distances

#计算标准差
def stdDev(X):
    '''假定X是一个数字列表
       返回X的标准差'''
    mean=float(sum(X)/len(X))
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

#变异系数＝标准差／平均值
def CV(X):
    mean=sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

def drunkTest(walkLenghths,numTrials,dClass):
    '''假定numTrials是大于等于0的整数， dClass是 Drunk的子类， 对于walkLenghths的每种步长，
       运行numTrials次实验并办理出结果'''
    for numSteps in walkLenghths:
        distances=simWalks(numSteps,numTrials,dClass)
        print dClass.__name__,'random walk of',numSteps,'steps'
        print 'Mean=',sum(distances)/len(distances),'CV=',CV(distances)
        print 'Max=',max(distances),'Min=',min(distances)


drunkTest((10,100,1000,10000),100,UsualDrunk)
