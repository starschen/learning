#encoding:utf8
#16_2图表会骗人.py
#绘制房价
import pylab
def plotHousing(impression):
    '''假设impression是一个字符串，必须是‘flat’， ‘volatile’或者是‘fair’
       生成房价随时间变化的图表'''
    f=open('midWestHousingPrices.txt','r')
    #文件的每一行是年季度价格
    #数据来自美国中部区域
    labels,prices=([],[])
    for line in f:
        year,quarter,price=line.split(' ')
        label=year[2:4]+'\n Q'+quarter[1]
        labels.append(label)
        prices.append(float(price)/1000)
    quarters=pylab.arange(len(labels))
    width=0.8
    if impression=='flat':
        pylab.semilogy()
    pylab.bar(quarters,prices,width)
    pylab.xticks(quarters+width/2.0,labels)
    pylab.title('Housing Prices in U.S. Midwest')
    pylab.xlabel('Quarter')
    pylab.ylabel('Average Price($1,000\'s)')
    if impression=='flat':
        pylab.ylim(10,10**3)
    elif impression =='volatile':
        pylab.ylim(180,220)
    elif impression=='fair':
        pylab.ylim(150,250)
    else:
        raise ValueError

plotHousing('flat')
pylab.figure()
plotHousing('volatile')
pylab.figure()
plotHousing('fair')
pylab.show()
