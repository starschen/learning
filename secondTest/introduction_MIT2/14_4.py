import random
def stdDev(X):
    mean=float(sum(X))/len(X)
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedls):
    inCircle=0
    for Needles in xrange(1,numNeedls+1):
        x=random.random()
        y=random.random()
        if (x*x+y*y)**0.5<=1.0:
            inCircle+=1
    return 4*(inCircle/float(numNeedls))

def getEst(numNeedls,numTrials):
    estimates=[]
    for t in xrange(numTrials):
        piGuess=throwNeedles(numNeedls)
        estimates.append(piGuess)
    sDev=stdDev(estimates)
    curEst=sum(estimates)/len(estimates)
    print 'Est.='+str(round(curEst,5))+',Std.dev.='+str(round(sDev,5))+', Needles='+str(numNeedls)
    return(curEst,sDev)

def estPi(precision,numTrials):
    numNeedls=1000
    sDev=precision
    while sDev>=precision/2.0:
        curEst,sDev=getEst(numNeedls,numTrials)
        numNeedls*=2
    return curEst

estPi(0.001,100)
