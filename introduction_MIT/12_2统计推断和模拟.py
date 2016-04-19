#encoding:utf8
#12.2统计推断和模拟

# 抛硬币
import random
import pylab
import math
def flip(numFlips):
    heads=0.0
    for i in range(numFlips):
        if random.random()<0.5:
            heads+=1
    return heads/numFlips

def flipsim(numFlipsPerTrial,numTrials):
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean=sum(fracHeads)/len(fracHeads)
    return mean

# m=int(raw_input('numFlips='))
# n=int(raw_input('numTrials='))
# print flipsim(m,n)

#用图表显示出抛硬币的结果
def flipPlot(minExp,maxExp):
    '''假定minExp和maxExp是正整数，并且minExp＜maxExp，
       绘制出2**minExp到2**maxExp次抛硬币的结果'''
    ratios=[]
    diffs=[]
    xAxis=[]
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads=0
        for n in range(numFlips):
            if random.random()<0.5:
                numHeads+=1
        numTails=numFlips-numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads-numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.semilogx()
    pylab.semilogy()
    pylab.ylabel('Abs(#Heads-#Tails)')
    pylab.plot(xAxis,diffs,'bo')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.semilogx()
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis,ratios,'bo')

# random.seed(0)
# flipPlot(4,20)
# pylab.show()

#计算标准差
def stdDev(X):
    '''假定X是一个数字列表
       返回X的标准差'''
    mean=float(sum(X)/len(X))
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

#模拟抛硬币
def makePlot(xvals,yvals,title,xlabel,ylabel,style,logX=False,logY=False):
    '''用给定的标题和标签绘制xvals,yvals'''
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.plot(xvals,yvals,style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()

def runTrial(numFlips):
    numHeads=0
    for n in range(numFlips):
        if random.random()<0.5:
            numHeads+=1
    numTails=numFlips-numHeads
    return (numHeads,numTails)

def filpPlot1(minExp,maxExp,numTrials):
    '''假定minExp和maxExp是正整数，并且minExp＜maxExp，
       绘制出2**minExp到2**maxExp次抛硬币的结果'''
    ratiosMeans,diffsMeans,ratiosSDs,diffsSDS=[],[],[],[]
    xAxis=[]
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios=[]
        diffs=[]
        for t in range(numTrials):
            numHeads,numTails=runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/float(numTrials))
        diffsMeans.append(sum(diffs)/float(numTrials))
        ratiosSDs.append(stdDev(ratios))
        diffsSDS.append(stdDev(diffs))
    numTrialsString='('+str(numTrials)+'Trials)'
    title='Mean Heads/Tails Ratios'+numTrialsString
    makePlot(xAxis,ratiosMeans,title,'Number of flips','Mean heads/Tails','bo',logX=True)
    title='SD Heads/Tails Ratios'+numTrialsString
    makePlot(xAxis,ratiosSDs,title,'Number of Flips','Standard Deviation','bo',logX=True,logY=True)
    #正面和反面数量的绝对差值
    title='Mean abs(Heads-Tails)'+numTrialsString
    makePlot(xAxis,diffsMeans,title,'Number of Flips','Mean abs(Heads-Tails)','bo',logX=True,logY=True)
    title='SD abs(HEads-Tails)'+numTrialsString
    makePlot(xAxis,diffsSDS,title,'Number of Flips','Standard Deviation','bo',logX=True,logY=True)

#变异系数＝标准差／平均值
def CV(X):
    mean=sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

filpPlot1(4,20,20)
pylab.show()
