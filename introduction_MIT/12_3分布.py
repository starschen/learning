#encoding:utf8
#12.3分布

import random
import pylab
# vals=[1,200]
# for i in range(1000):
#     num1=random.choice(range(1,100))
#     num2=random.choice(range(1,100))
#     vals.append(num1+num2)
# pylab.hist(vals,bins=10)

#绘制抛硬币的正态分布直方图
import math
def flip(numFlips):
    heads=0.0
    for i in range(numFlips):
        if random.random()<0.5:
            heads+=1
    return heads/numFlips
#计算标准差
def stdDev(X):
    '''假定X是一个数字列表
       返回X的标准差'''
    mean=float(sum(X)/len(X))
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

def flipsim(numFlipsPerTrial,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean=sum(fracHeads)/len(fracHeads)
    sd=stdDev(fracHeads)
    return (fracHeads,mean,sd)

def labelPlot(numFlips,numTrials,mean,sd):
    pylab.title(str(numTrials)+'trials of'+str(numFlips)+'flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin,xmax=pylab.xlim()
    ymin,ymax=pylab.ylim()
    pylab.text(xmin+(xmax-xmin)*0.02,(ymax-ymin)/2,'Mean='+str(round(mean,4))+'\nSD='+str(round(sd,4)),size='x-large')

def makePlots(numFlips1,numFlips2,numTrials):
    val1,mean1,sd1=flipsim(numFlips1,numTrials)
    pylab.hist(val1,bins=20)
    xmin,xmax=pylab.xlim()
    ymin,ymax=pylab.ylim()
    labelPlot(numFlips1,numTrials,mean1,sd1)
    pylab.figure()
    val2,mean2,sd2=flipsim(numFlips2,numTrials)
    pylab.hist(val2,bins=20)
    pylab.xlim(xmin,xmax)
    labelPlot(numFlips2,numTrials,mean2,sd2)


# random.seed(0)
# makePlots(100,1000,100000)
# pylab.show()

#绘制误差线
def showErrorBars(minExp,maxExp,numTrials):
    means,sds=[],[]
    xvals=[]
    for exp in range(minExp,maxExp+1):
        xvals.append(2**exp)
        fracHeads,mean,sd=flipsim(2**exp,numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.semilogx()
    pylab.title('Mean Fraction of HEads('+str(numTrials)+'trials)')
    pylab.xlabel('Number of flips per trial')
    pylab.ylabel('Fraction of heads & 95% confidence')
    pylab.errorbar(xvals,means,yerr=2*pylab.array(sds))
#
# showErrorBars(3,10,100)
# pylab.show()

#分子清除指数分布
def clear(n,p,steps):
    '''假定n和steps是正整数，p是浮点数，n是分子的初始数量，p是分子被清的概率，steps是模拟时间'''
    numRemaining=[n]
    for t in range(steps):
        numRemaining.append(n*(1-p)**t)
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')

# clear(100,0.01,1000)
# pylab.show()

#几何分布
def successfulStars(eventProb,numTrials):
    '''假设eventProb是一个浮点数，表示每次尝试成功的几率，numTrials是正整数
       返回每次实验成功前需要尝 试的次数列表。'''
    triesBeforeSuccess=[]
    for t in range(numTrials):
        consecFailures=0
        while random.random()>eventProb:
            consecFailures+=1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

random.seed(0)
probOfSuccess=0.5
numTrials=5000
distribution=successfulStars(probOfSuccess,numTrials)
pylab.hist(distribution,bins=14)
pylab.xlabel('Tries Before Success')
pylab.ylabel('Number of Occurrences Out of'+str(numTrials))
pylab.title('Probability of Starting Each Try'+str(probOfSuccess))
pylab.show()
