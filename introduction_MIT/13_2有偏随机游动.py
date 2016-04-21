#encoding:utf8
#13.2有偏随机游动

#Drunk的子类
##13.1醉汉游动
import random
import pylab
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
#new
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,1.0),(0.0,-2.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)

# def simAll(drunkKinds,walkLengths,numTrials):
#     for dClass in drunkKinds:
#         drunkTest(walkLengths,numTrials,dClass)

#醉汉游动
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

def drunkTest(walkLengths,numTrials,dClass):
    '''假定numTrials是大于等于0的整数， dClass是 Drunk的子类， 对于walkLengths的每种步长，
       运行numTrials次实验并办理出结果'''
    for numSteps in walkLengths:
        distances=simWalks(numSteps,numTrials,dClass)
        print dClass.__name__,'random walk of',numSteps,'steps'
        print 'Mean=',sum(distances)/len(distances),'CV=',CV(distances)
        print 'Max=',max(distances),'Min=',min(distances)
        print ''

# simAll((UsualDrunk,ColdDrunk,EWDrunk),(100,1000),10)

#遍历风格
class styleIterator(object):
    def __init__(self,styles):
        self.index=0
        self.styles=styles

    def nextStyle(self):
        result=self.styles[self.index]
        if self.index==len(self.styles)-1:
            self.index=0
        else:
            self.index+=1
        return result

#绘制不同类型醉汉的游动
def simDrunk(numTrials,dClass,walkLengths):
    meanDistances=[]
    cvDistances=[]
    for numSteps in walkLengths:
        print 'Starting simulation of',numSteps,'steps'
        trials=simWalks(numSteps,numTrials,dClass)
        mean=sum(trials)/float(len(trials))
        meanDistances.append(mean)
        cvDistances.append(stdDev(trials)/mean)
    return (meanDistances,cvDistances)

def simAll(drunkKinds,walkLengths,numTrials):
    styleChoice=styleIterator(('b-','r:','m-.'))
    for dClass in drunkKinds:
        curStyle=styleChoice.nextStyle()
        print 'Starting simulation of',dClass.__name__
        means,cvs=simDrunk(numTrials,dClass,walkLengths)
        cvMean=sum(cvs)/float(len(cvs))
        pylab.plot(walkLengths,means,curStyle,label=dClass.__name__+'(CV='+str(round(cvMean,4))+')')
    pylab.title('Mean Distance from Origin('+str(numTrials)+'trials)')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.semilogx()
    pylab.semilogy()

# simAll((UsualDrunk,ColdDrunk,EWDrunk),(10,100,1000,10000,100000),100)
# pylab.show()

#绘制最终位置
def getFinalLocs(numSteps,numTrials,dClass):
    locs=[]
    d=dClass()
    origin=Location(0,0)
    for t in range(numTrials):
        f=Field()
        f.addDrunk(d,origin)
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds,numSteps,numTrials):
    styleChoice=styleIterator(('b+','r^','mo'))
    for dClass in drunkKinds:
        locs=getFinalLocs(numSteps,numTrials,dClass)
        xVals,yVals=[],[]
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        meanX=sum(xVals)/float(len(xVals))
        meanY=sum(yVals)/float(len(yVals))
        curStyle=styleChoice.nextStyle()
        pylab.plot(xVals,yVals,curStyle,label=dClass.__name__+'Mean loc.=<'+str(meanX)+','+str(meanY)+'>')
    pylab.title('Location at End of Walks('+str(numSteps)+'steps)')
    pylab.xlabel('Steps east/west of origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc= 'lower left',numpoints=1)

# plotLocs((UsualDrunk,ColdDrunk,EWDrunk),100,200)
# pylab.show()

#跟踪游动
def tracWalk(drunkKinds,numSteps):
    styleChoice=styleIterator(('b+','r^','mo'))
    f=Field()
    for dClass in drunkKinds:
        d=dClass()
        f.addDrunk(d,Location(0,0))
        locs=[]
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals=[]
        yVals=[]
        for l in locs:
            xVals.append(l.getX())
            yVals.append(l.getY())
        curStyle=styleChoice.nextStyle()
        pylab.plot(xVals,yVals,curStyle,label=dClass.__name__)
    pylab.title('Spots Visited on Walk ('+str(numSteps)+'steps)')
    pylab.xlabel('Steps east/west of origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc= 'best')

tracWalk((UsualDrunk,ColdDrunk,EWDrunk),200)
pylab.show()
