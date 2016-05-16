import random
# def flip(numFlips):
#     heads=0.0
#     for i in range(numFlips):
#         if random.random()<0.5:
#             heads+=1
#     return heads/numFlips
#
# def flipSim(numFlipsPerTrial,numTrials):
#     fracHeads=[]
#     for i in range(numTrials):
#         fracHeads.append(flip(numFlipsPerTrial))
#     mean=sum(fracHeads)/len(fracHeads)
#     return mean

# print flipSim(100,1)
# print flipSim(100,1)
# print flipSim(100,100)
# print flipSim(100,10000)
# print flipSim(100,1000000)

import pylab
# def flipPlot(minExp,maxExp):
#     ratios=[]
#     diffs=[]
#     xAixs=[]
#     for exp in range(minExp,maxExp+1):
#         xAixs.append(2**exp)
#     for numFlips in xAixs:
#         numHeads=0
#         for i in range(numFlips):
#             if random.random()<0.5:
#                 numHeads+=1
#         numTails=numFlips-numHeads
#         ratios.append(numHeads/float(numTails))
#         diffs.append(abs(numHeads-numTails))
#     pylab.title('Difference Between Heads and Tails')
#     pylab.xlabel('Number of Flips')
#     pylab.ylabel('Abs(#Heads-#Tails)')
#     pylab.plot(xAixs,diffs,'bo')
#     pylab.semilogx()
#     pylab.semilogy()
#     pylab.figure()
#     pylab.title('Heads/Tails Ratios')
#     pylab.xlabel('Number of Flips')
#     pylab.ylabel('#Heads/#Tails')
#     pylab.semilogx()
#     pylab.plot(xAixs,ratios,'bo')
#
# random.seed(0)
# flipPlot(4,20)
# pylab.show()

def stdDev(X):
    mean=float(sum(X))/len(X)
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

def makePlot(xVals,yVals,title,xLabel,yLabel,style,logX=False,logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals,yVals,style)
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

def CV(X):
    mean=sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

def flipPlot1(minExp,maxExp,numTrials):
    ratiosMeans,diffsMeans,ratiosSDs,diffsSDs,ratiosCV,diffsCV=[],[],[],[],[],[]
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
        diffsSDs.append(stdDev(diffs))
        ratiosCV.append(CV(ratios))
        diffsCV.append(CV(diffs))
    numTrialsString='('+str(numTrials)+'Trails)'
    title='Mean Heads/Tails Ratios'+numTrialsString
    makePlot(xAxis,ratiosMeans,title,'Number of Flips','Mean Heads/Tails','bo',logX=True)
    pylab.savefig('12_2Mean Heads Tails Ratios')
    title='SD Heads/Tails Ratios'+numTrialsString
    makePlot(xAxis,ratiosSDs,title,'Number of Flips','Standard Deviation','bo',logX=True,logY=True)
    pylab.savefig('12_2SD Heads Tails Ratios')
    title='Mean abs(#Heads-#Tails)'+numTrialsString
    makePlot(xAxis,diffsMeans,title,'Number of Flips','Mean abs(#Heads-#Tails)','bo',logX=True,logY=True)
    pylab.savefig('12_2Mean Heads-Tails')
    title='SD abs(#Heads-#Tails)'+numTrialsString
    makePlot(xAxis,diffsSDs,title,'Number of Flips','SD abs(#Heads-#Tails)','bo',logX=True,logY=True)
    pylab.savefig('12_2SD Heads-Tails')
    title='Coeff. of Var. abs(Heads-Tails)'+numTrialsString
    makePlot(xAxis,diffsCV,title,'Number of Flips','Coeff. of Var. abs(Heads-Tails)','bo',logX=True)
    pylab.savefig('12_2Coeff of Var Heads-Tails')
    title='Coeff. of Var. Heads/Tails Ratio'+numTrialsString
    makePlot(xAxis,ratiosCV,title,'Number of Flips','Coeff. of Var. Heads/Tails Ratio','bo',logX=True,logY=True)
    pylab.savefig('12_2Coeff of Var Heads Tails Ratio')
flipPlot1(4,20,20)
pylab.show()
