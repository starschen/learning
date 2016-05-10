#encoding:utf8

def findPayment(loan,r,m): #loan and r are float,r is ratio,m is month
    return loan*(r*(1+r)**m)/((1+r)**m-1)   #return loan per month to pay back

class Mortgage(object):
    def __init__(self,loan,annRate,months):
        self.loan=loan
        self.rate=annRate/12.0
        self.months=months
        self.paid=[0]
        self.owed=[loan]
        self.payment=findPayment(loan,self.rate,months)
        self.legend=None

    def makePayment(self):
        self.paid.append(self.payment)
        reduction=self.payment-self.owed[-1]*self.rate
        self.owed.append(self.owed[-1]-reduction)

    def getTotalPaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend
