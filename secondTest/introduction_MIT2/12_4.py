import random
import pylab
def playSeries(numGames,teamProb):
    numWon=0
    for game in range(numGames):
        if random.random()<=teamProb:
            numWon+=1
    return (numWon>numGames//2)

def simSeries(numSeries):
    prob=0.5
    fracWon=[]
    probs=[]
    while prob<=1.0:
        seriesWon=0.0
        for i in range(numSeries):
            if playSeries(7,prob):
                seriesWon+=1
        fracWon.append(seriesWon/numSeries)
        probs.append(prob)
        prob+=0.01
    pylab.plot(probs,fracWon,linewidth=5)
    pylab.xlabel('Probability of Winning a Game')
    pylab.ylabel('Probability of Winning a Series')
    pylab.axhline(0.95)
    pylab.ylim(0.5,1.1)
    pylab.title(str(numSeries)+'Seven-Game Series')
    pylab.savefig('12_4seven_game')

# simSeries(400)
# pylab.show()

def findSeriesLength(teamProb):
    numSeries=200
    maxLen=2500
    step=10

    def fracWon(teamProb,numSeries,seriesLen):
        won=0.0
        for series in range(numSeries):
            if playSeries(seriesLen,teamProb):
                won+=1
        return won/numSeries

    winFrac=[]
    xVals=[]
    for seriesLen in range(1,maxLen,step):
        xVals.append(seriesLen)
        winFrac.append(fracWon(teamProb,numSeries,seriesLen))
    pylab.plot(xVals,winFrac,linewidth=5)
    pylab.xlabel('Length of Series')
    pylab.ylabel('Probability of Winning Series')
    pylab.ylim(0.4,1.1)
    pylab.title(str(round(teamProb,4))+'Probability of Better Team Winning a Game')
    pylab.axhline(0.95)
    pylab.savefig('12_4findSeriesLength')

YanksProb=0.636
PhilsProb=0.574
findSeriesLength(YanksProb/(YanksProb+PhilsProb))
pylab.show()
