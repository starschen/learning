import random
def rollDie():
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials):
    numWins=0.0
    for j in range(numTrials):
        for i in range(24):
            d1=rollDie()
            d2=rollDie()
            if d1==6 and d2==6:
                numWins+=1
                break
    print 'Probability of winning =',numWins/numTrials

checkPascal(1000000)
