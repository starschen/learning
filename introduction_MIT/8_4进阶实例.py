#encoding:utf8
#8.4进阶实例：抵押贷款
##4.14代码有点问题，明天研究

#Mortgage基类
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
        self.legend='Fixed, '+ str(r*100)+'% ',+str(pts)+' points'

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

def compareMortgages(amt,years,fixedRate,pts,ptsRate,varRate1,varRate2,varMonths):
    totMonths=years*12
    fixed1=Fixed(amt,fixedRate,totMonths)
    fixed2=FixedWithPts(amt,ptsRate,totMonths,pts)
    twoRate=TwoRate(amt,ptsRate,totMonths,pts)
    morts=[fixed1,fixed2,twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print m
        print 'Total payments=$' +str(int(m.getTotalPaid()))

compareMortgages(amt=200000,years=30,fixedRate=0.07,pts=3.25,ptsRate=0.05,varRate1=0.045,varRate2=0.095,varMonths=48)
