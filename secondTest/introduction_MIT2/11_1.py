#encoding:utf8
import pylab

# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,7,3,5])
# pylab.show()

# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,2,3,4])
# pylab.figure(2)
# pylab.plot([1,4,2,3],[5,6,7,8])
# pylab.savefig('Figure-Addie')
# pylab.figure(1)
# pylab.plot([5,6,10,3])  #默认y值，x值为range（len（［5，6，10，3］）
# pylab.savefig('Figure-Jane')

principal=10000
interestRate=0.05
years=20
values=[]
for i in range(years+1):
    values.append(principal)
    principal+=principal*interestRate
pylab.plot(values,'ro')
pylab.title('5% Growth,Compounded Annually',fontsize='xx-large')
pylab.xlabel('Years of Compounding',fontsize='x-small')
pylab.ylabel('Value of Principal ($)')
pylab.savefig('Figure-11_1_3')
pylab.show()
