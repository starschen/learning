import pylab
def plotHousing(impression):
    f=open('midWestHousingPrices.txt','r')
    labels,prices=[],[]
    for line in f:
        year,quarter,price=line.split(' ')
        label=year[2:4]+'\n'+quarter[:]
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
    pylab.ylabel('Average Price ($1000\'s)')
    if impression=='flat':
        pylab.ylim(10,10**3)
    elif impression=='volatile':
        pylab.ylim(180,220)
    elif impression=='fair':
        pylab.ylim(150,250)
    else:
        raise ValueError

plotHousing('flat')
pylab.savefig('16_2flat')
pylab.figure()
plotHousing('volatile')
pylab.savefig('16_2volatile')
pylab.figure()
plotHousing('fair')
pylab.savefig('16_2fair')
pylab.show()
