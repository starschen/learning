import random
def stdDev(X):
    mean=float(sum(X))/len(X)
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

def CV(X):
    mean=sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

class Location(object):

    def __init__(self,x,y):
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
        self.drunks[drunk]=currentLocation.move(xDist,yDist)

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

class Drunk(object):
    def __init__(self,name=None):
        self.name=name

    def __str__(self):
        if self!=None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoice=[(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoice)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoice=[(0.0,1.0),(0.0,-2.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoice)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoice=[(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoice)

def walk(f,d,numSteps):
    start=f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps,numTrials,dClass):
    Homer=dClass()
    origin=Location(0.0,0.0)
    distances=[]
    for t in range(numTrials):
        f=Field()
        f.addDrunk(Homer,origin)
        distances.append(walk(f,Homer,numSteps))
    return distances

def drunkTest(walkLengths,numTrials,dClass):
    for numSteps in walkLengths:
        distances=simWalks(numSteps,numTrials,dClass)
        print dClass.__name__,'random walk of',numSteps,'steps:'
        print 'Mean=',sum(distances)/len(distances),'CV=',CV(distances)
        print 'Max=',max(distances),'Min=',min(distances)
        print ''

# drunkTest((10,100,1000,10000),100,UsualDrunk)


def simAll(drunkKinds,walkLengths,numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths,numTrials,dClass)

simAll((UsualDrunk,ColdDrunk,EWDrunk),(100,1000),10)

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
