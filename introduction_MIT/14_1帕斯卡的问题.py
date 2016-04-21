#encoding:utf8
#14.1帕斯卡的问题
#检验帕斯卡的分析
import random
def rollDie():
    return random.choice([1,2,3,4,5,6])

def chekPascal(numTrials):
    '''假设numTrials是一个正整数，输出获胜的概率'''
    numWins=0.0
    for i in range(numTrials):
        for j in range(24):
            d1=rollDie()
            d2=rollDie()
            if d1==6 and d2==6:
                numWins+=1
                break
    print 'Probability of winning=',numWins/numTrials

chekPascal(1000000)
