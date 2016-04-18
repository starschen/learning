#encoding:utf8
#11.2扩展实例：绘制抵押贷款


##4.18用的8－4的代码，还是有问题，
import pylab
def findPayment(loan,r,m):
    """假定：loan和r都是浮点数，m是整数
       返回贷款数为loan、每月利率为r，共m个月情况下的每月还款数"""
    return loan*((r*(1+r)**m)/(1+r)**m-1)

class Mortgage(object):
    """用来构建不同类型抵押贷款的抽象类"""
    def __init__(self,loan,annRate,months):
        """创建一个抵押贷款"""
        self.loan=loan
        self.rate=annRate/12.0
        self.months=months
        self.paid=[0.0]
        self.owed=[loan]
        self.payment=findPayment(loan,self.rate,months)
        self.legend=None  #description of Mortgage

    def makePayment(self):
        """还款"""
        self.paid.append(self.payment)
        reduction=self.payment-self.owed[-1]*self.rate
        self.owed.append(self.owed[-1]-reduction)

    def getTotalPaid(self):
        """返回现在总还款数"""
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plotpayments(self,style):
        pylab.plot(self.paid[1:],style,label=self.legend)

    def plotbalance(self,style):
        pylab.plot(self.owed,style,label=self.legend)

    def plottotpd(self,style):
        '''绘制还款总额的变化'''
        totpd=[self.paid[0]]
        for i in range(1,len(self.paid)):
            totpd.append(totpd[-1]+self.paid[i])
        pylab.plot(totpd,style,label=self.legend)

    def plotnet(self,style):
        '''绘制抵押贷款大致的总支出，用现金支出减去通过还清部分贷款所得的本金'''
        totpd=[self.paid[0]]
        for i in range(1,len(self.paid)):
            totpd.append(totpd[-1]+self.paid[i])
        #通过还贷所得的本金就是到现在为止获得的原始贷款总额，也就是总贷款额减去现有贷款
        equityacquied=pylab.array([self.loan]*len(self.owed))
        equityacquied=equityacquied-pylab.array(self.owed)
        net=pylab.array(totpd)-equityacquied
        pylab.plot(net,style,label=self.legend)

#固定费率货款类
class Fixed(Mortgage):
    def __init__(self,loan,r,months):
        Mortgage.__init__(self,loan,r,months)
        self.legend='Fixed, '+str(r*100)+'%'

class FixedWithPts(Mortgage):
    def __init__(self,loan,r,months,pts):
        Mortgage.__init__(self,loan,r,months)
        self.pts=pts
        self.paid=[loan*(pts/100.0)]
        self.legend='Fixed, '+ str(r*100)+'% ',+str(pts)+' points'  #str 一直报错

#包含引诱费率的抵押贷款
class TwoRate(Mortgage):
    def __init__(self,loan,r,months,teaserRate,teaserMonths):
        Mortgage.__init__(self,loan,teaserRate,months)
        self.teaserMonths=teaserMonths
        self.teaserRate=teaserRate
        self.nextRate=r/12.0
        self.legend=str(teaserRate*100)+' months,then '+str(r*100) +'%'

    def makePayment(self):
        if len(self.paid)==self.teaserMonths+1:
            self.rate=self.nextRate
            self.payment=findPayment(self.owed[-1],self.rate,self.months-self.teaserMonths)

        Mortgage.makePayment(self)


def plotmortagages(morts,ame):
    styles=['b-','b-','b:']
    payments=0
    cost=1
    balance=2
    netcost=3
    pylab.figure(payments)
    pylab.title('Monthly Payments of Different $'+'Mortagages')
    pylab.xlabel('months')
    pylab.ylabel('months payments')

    pylab.figure(cost)
    pylab.title('Cash OUtlay of different $'+str(amt)+'Mortagages')
    pylab.xlabel('months')
    pylab.ylabel('Total Payments')

    pylab.figure(balance)
    pylab.title('Balance Remaining of $'+str(amt)+'Mortagages')
    pylab.xlabel('months')
    pylab.ylabel('Remaining Loan Balance of $')

    pylab.figure(netcost)
    pylab.title('Net Cost of $'+str(amt)+'Mortagages')
    pylab.xlabel('months')
    pylab.ylabel('Payments-Equity $')

    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotpayments(styles[i])
        pylab.figure(cost)
        morts[i].plottotpd(styles[i])
        pylab.figure(balance)
        morts[i].plotbalance(styles[i])
        pylab.figure(netcost)
        morts[i].plotnet(styles[i])
    pylab.figure(payments)
    pylab.legend(loc='upper center')
    pylab.figure(cost)
    pylab.legend(loc='best')
    pylab.figure(balance)
    pylab.legend(loc='best')

def compareMortgages(amt,years,fixedRate,pts,ptsRate,varRate1,varRate2,varMonths):
    totMonths=years*12
    fixed1=Fixed(amt,fixedRate,totMonths)
    fixed2=FixedWithPts(amt,ptsRate,totMonths,pts)
    twoRate=TwoRate(amt,varRate2,totMonths,varRate1,varMonths)
    morts=[fixed1,fixed2,twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotmortagages(morts,amt)

compareMortgages(amt=200000,years=30,fixedRate=0.07,pts=3.25,ptsRate=0.05,
                 varRate1=0.045,varRate2=0.095,varMonths=48)
