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

# pylab.savefig('15_3fitIndex')
# pylab.show()

# pred2to20=a*(20**4)+b*(20**3)+c*(20**2)+d*20+e
# print 'Model predicts that 2**20 is roughly',round(pred2to20)
# print 'Actual value of 2**20 is', 2**20

xVals,yVals=[],[]
for i in range(10):
    xVals.append(i)
    yVals.append(2**i)
pylab.plot(xVals,yVals)
pylab.semilogy()
pylab.show()
