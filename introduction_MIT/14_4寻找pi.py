#encoding:utf8
#14.4寻找pi

import random
#计算标准差
def stdDev(X):
    '''假定X是一个数字列表
       返回X的标准差'''
    mean=float(sum(X)/len(X))
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle=0
    for Needles in xrange(1,numNeedles+1):
        x=random.random()
        y=random.random()
        if (x*x+y*y)**0.5<=1.0:
            inCircle+=1
    return 4*(inCircle/float(numNeedles)) #因为计算的针尖只在一个象限中的情况，所以要＊4
    # return 2*(inCircle/float(numNeedles))

def getEst(numNeedles,numTrials):
    estimates=[]
    for t in range(numTrials):
        piGuess=throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev=stdDev(estimates)
    curEst=sum(estimates)/len(estimates)
    print 'Est.='+str(round(curEst,5))+',Std.dev.='+str(round(sDev,5))+',Needles='+str(numNeedles)
    return (curEst,sDev)

def estPi(precision,numTrials):
    numNeedles=1000
    sDev=precision
    while sDev>=precision/2.0:
        curEst,sDev=getEst(numNeedles,numTrials)
        numNeedles*=2
    return curEst

estPi(0.01,100)
