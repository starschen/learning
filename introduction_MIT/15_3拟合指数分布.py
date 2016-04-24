#encoding:utf8
#15_3拟合指数分布.py
#用多项式曲线来拟合指数分布
import pylab
# vals=[]
# for i in range(10):
#     vals.append(2**i)
# pylab.plot(vals,'bo',label='Actual points')
# xVals=pylab.arange(10)
# a,b,c,d,e=pylab.polyfit(xVals,vals,4)
# yVals=a*(xVals**4)+b*(xVals**3)+c*(xVals**2)+d*xVals+e
# pylab.plot(yVals,'bx',label='Predicted points',markersize=20)
# pylab.title('Fitting y=2**x')
# pylab.legend()
# # pylab.show()
#
# pred2to20=a*(20**4)+b*(20**3)+c*(20**2)+d*20+e
# # print 'Model predicts that 2**20 is roughtly',round(pred2to20)
# # print 'Actual value of 2**20 is',2**20
#
# xVals,yVals=[],[]
# for i in range(10):
#     xVals.append(i)
#     yVals.append(2**i)
# pylab.plot(xVals,yVals)
# pylab.semilogy()
# # pylab.show()

#使用polyfit拟合指数分布
import math

#定义一个指数函数
def f(x):
    return 3*(2**(1.2*x))    #初始数据可以用函数y=base**(a*x+b)表示
    # return 3*(2**(1.2*x))+x  #不能用上式表示

def createExpData(f,xVals):
    '''假设f是只有一个参数的指数函数， xVals是一个数组，其中的值可以作为参数传入f
       返回一个数组，包含xVals中的元素传入f生成的结果'''
    yVals=[]
    for i in range(len(xVals)):
        yVals.append(f(xVals[i]))
    return pylab.array(xVals),pylab.array(yVals)

def fitExpData(xVals,yVals):
    '''假设xVals和yVals是数字数组并且满足yVals[i]==f(xVals[i])
       返回a,b,base，满足log(f(x),base)==ax+b'''
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
pylab.show()
#查找一个不在原始数据中的x值
print 'f(20)=',f(20)
print 'Predicted f(20)=',base**(a*20+b)
