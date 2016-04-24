#encoding:utf8
#16_8得克萨斯神枪手的谬误.py
import random
#六月有48个神经性厌食症患者出生的概率
def juneProb(numTrials):
    june48=0
    for trial in range(numTrials):
        june=0
        for i in range(446):
            if random.choice([1,2,3,4,5,6,7,8,9,10,11,12]) == 6:
                june+=1
        if june>=48:
            june48+=1
    jProb=june48/float(numTrials)
    print 'Probability of at least 48 births in june=',jProb

# juneProb(10000)

#某个月出现48个患神经性厌食症新生儿的概率
def anyProb(numTrials):
    anyMonth48=0
    for trial in range(numTrials):
        months=[0]*12
        for i in range(446):
            months[random.choice([0,1,2,3,4,5,6,7,8,9,10,11])]+=1
        if max(months)>=48:
            anyMonth48+=1
    aProb=anyMonth48/float(numTrials)
    print 'Probability of at least 48 births in some month=',aProb

anyProb(10000)
