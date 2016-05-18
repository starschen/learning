import random
import pylab
def collisionProb(n,k):
    prob=1.0
    for i in range(1,k):
        prob=prob*(n-i)/float(n)
    return 1-prob

# print collisionProb(1000,50)
# print collisionProb(1000,200)

def simInsertions(numIndices,numInsertions):
    choices=range(numIndices)
    used=[]
    for i in range(numInsertions):
        hashVal=random.choice(choices)
        if hashVal in used:
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices,numInsertions,numTrials):
    collisons=0.0
    for i in range(numTrials):
        collisons+=simInsertions(numIndices,numInsertions)
    return collisons/numTrials

print 'Actual probability of a collision =',collisionProb(1000,50)
print 'Est. probability of a collision =',findProb(1000,50,10000)
print 'Actual probability of a collision =',collisionProb(1000,200)
print 'Est. probability of a collision =',findProb(1000,200,10000)
