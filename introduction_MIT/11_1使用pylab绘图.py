#encoding:utf8
#11.1使用pylab绘图

import pylab


# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,7,3,5])
# pylab.show()

principal=10000
interestrate=0.05
years=20
values=[]
for i in range(years+1):
    values.append(principal)
    principal+=principal*interestrate
pylab.plot(values,linewidth=5)
pylab.title('5% Growth,Compounded Annually',fontsize='xx-large')
pylab.xlabel('Years of Compounded',fontsize='x-small')
pylab.ylabel('Value of principal($)')
pylab.show()
