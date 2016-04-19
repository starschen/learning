#encoding:utf8
#12.5散列和碰撞

import random
import pylab
#散列表至少发生一次碰撞的概率
def collisionProb(n,k):
    prob=1.0
    for i in range(1,k):
        prob=prob*((n-i)/float(n))
    return 1-prob

print collisionProb(1000,50)

#模拟散列表
def simInsertions(numIndices,numInsertions):
    '''假设numIndices,numInsertions是正整数，如果发生碰撞返回1，否则返回0'''
    choices=range(numIndices)
    used=[]
    for i in range(numInsertions):
        hashval=random.choice(choices)
        if hashval in used:
            return 1
        else:
            used.append(hashval)
    return 0

def findProb(numIndices,numInsertions,numTrials):
    collisions=0.0
    for t in range(numTrials):
        collisions+=simInsertions(numIndices,numInsertions)
    return collisions/numTrials

print 'Actual probability of a collision=',collisionProb(1000,50)
print 'Est. probability of a collision=',findProb(1000,50,10000)
print 'Actual probability of a collision=',collisionProb(1000,200)
print 'Est. probability of a collision=',findProb(1000,200,10000)
