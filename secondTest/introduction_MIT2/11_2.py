#encoding:utf8
import pylab
def findPayment(loan,r,m): #loan and r are float,r is ratio,m is month
    return loan*(r*(1+r)**m)/((1+r)**m-1)   #return loan per month to pay back
    #

class Mortgage(object):
    '''用来生成不同类型贷款的抽象类'''
    def __init__(self,loan,annRate,months):
        '''创建一个新贷款'''
        self.loan=loan#欠款总额
        self.rate=annRate/12.0 #月利率＝年利率／12
        self.months=months#总月份
        self.paid=[0.0]#已还款列表
        self.owed=[loan]#仍欠款列表
        self.payment=findPayment(loan,self.rate,months)#每月要还的钱
        self.legend=None#对子类的描述

    def makePayment(self):
        '''还款'''
        self.paid.append(self.payment)
        reduction=self.payment-self.owed[-1]*self.rate#????
        self.owed.append(self.owed[-1]-reduction)#????

    def getTotalPaid(self):
        '''返回到目前为止的总还款额'''
        return sum(self.paid)#

    def __str__(self):
        return self.legend

    def plotPayments(self,style):
        pylab.plot(self.paid[1:],style,label=self.legend)

    def plotBalance(self,style):
        pylab.plot(self.owed,style,label=self.legend)

    def plotTotPd(self,style):
        '''绘制还款总额的变化'''
        totPd=[self.paid[0]]
        for i in range(1,len(self.paid)):
            totPd.append(totPd[-1]+self.paid[i])
        pylab.plot(totPd,style,label=self.legend)

    def plotNet(self,style):
        '''绘制抵押贷款大致的总支出，用现金支出减去通过还清部分贷款所得的本金'''
        totPd=[self.paid[0]]
        for i in range(1,len(self.paid)):
            totPd.append(totPd[-1]+self.paid[i])
        #通过来贷所得的本金就是到现在为止获得的原始贷款总额，也就是总贷款额减去现有贷款
        equityAcquired=pylab.array([self.loan]*len(self.owed))
        equityAcquired=equityAcquired-pylab.array(self.owed)
        net=pylab.array(totPd)-equityAcquired
        pylab.plot(net,style,label=self.legend)

class Fixed(Mortgage):
    def __init__(self,loan,r,months):
        Mortgage.__init__(self,loan,r,months)
        self.legend='Fixed,'+str(r*100)+'%'

class FixedWithPts(Mortgage):
    def __init__(self,loan,r,months,pts):
        Mortgage.__init__(self,loan,r,months)
        self.pts=pts
        self.paid=[loan*(pts/100.0)]
        self.legend='Fixed,'+str(r*100)+'%,'+str(pts)+' points'

class TwoRate(Mortgage):
    def __init__(self,loan,r,months,teaserRate,teaserMonths):
        Mortgage.__init__(self,loan,teaserRate,months)
        self.teaserMonths=teaserMonths
        self.teaserRate=teaserRate
        self.nextRate=r/12.0
        self.legend=str(teaserRate*100)+'% for'+str(self.teaserMonths)+' months,then'+str(r*100)+'%'

    def makePayment(self):
        if len(self.paid)==self.teaserMonths+1:
            self.rate=self.nextRate
            self.payment=findPayment(self.owed[-1],self.rate,self.months-self.teaserMonths)

        Mortgage.makePayment(self)


def plotMortgages(morts,amt):
    styles=['b-','b-.','b:']
    payments=0
    cost=1
    balance=2
    netCost=3
    pylab.figure(payments)
    pylab.title('Monthly Payments of Different $'+str(amt)+' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Monthly Payments')

    pylab.figure(cost)
    pylab.title('Cash Outlay of Different $'+str(amt)+' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Total Payments')

    pylab.figure(balance)
    pylab.title('Balance Remaining of $'+str(amt)+' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Remaining Loan Balance of $')

    pylab.figure(netCost)
    pylab.title('Net Cost of $'+str(amt)+' Mortgage')
    pylab.xlabel('Months')
    pylab.ylabel('Payments-Equity $')

    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])
    pylab.figure(payments)
    pylab.legend(loc='upper center')
    pylab.savefig('11_2 payments')
    pylab.figure(cost)
    pylab.legend(loc='best')
    pylab.savefig('11_2 cost')
    pylab.figure(balance)
    pylab.legend(loc='best有疑问')
    pylab.savefig('11_2 balance')
    pylab.figure(netCost)
    pylab.savefig('11_2 netCost')

def compareMortgages(amt,years,fixedRate,pts,ptsRate,varRate1,varRate2,varMonths):
    totMonths=years*12
    fixed1=Fixed(amt,fixedRate,totMonths)
    fixed2=FixedWithPts(amt,ptsRate,totMonths,pts)
    twoRate=TwoRate(amt,varRate2,totMonths,varRate1,varMonths)
    morts=[fixed1,fixed2,twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts,amt)

compareMortgages(amt=200000,years=30,fixedRate=0.07,pts=3.25,ptsRate=0.05,varRate1=0.045,varRate2=0.095,varMonths=48)
pylab.show()
