import pylab
import math

def f(x):
    return 3*(2**(1.2*x))

def createExpData(f,xVals):
    yVals=[]
    for i in range(len(xVals)):
        yVals.append(f(xVals[i]))
    return pylab.array(xVals),pylab.array(yVals)

def fitExpData(xVals,yVals):
    logVals=[]
    for y in yVals:
        logVals.append(math.log(y,2.0))
    a,b=pylab.polyfit(xVals,logVals,1)
    return a,b,2.0

xVals,yVals=createExpData(f,range(10))
pylab.plot(xVals,yVals,'ro',label='Actual values')
a,b,base=fitExpData(xVals,yVals)
predictedYVals=[]
for x in xVals:
    predictedYVals.append(base**(a*x+b))
pylab.plot(xVals,predictedYVals,label='Predicted values')
pylab.title('Fitting an Exponential Function')
pylab.legend()
pylab.savefig('15_4fitlog')
print 'f(20)=',f(20)
print 'Predicted f(20)=', base**(a*20+b)
pylab.show()
