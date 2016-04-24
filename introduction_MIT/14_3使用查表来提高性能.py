#encoding:utf8
#14.3使用查表来提高性能
#14.2的crapsSim时间复杂度 O(playHand*handsPerGame*numGames)
#本题中的playHand 复杂度为O(1)
#another playHand
import random
#计算标准差
def stdDev(X):
    '''假定X是一个数字列表
       返回X的标准差'''
    mean=float(sum(X)/len(X))
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return (tot/len(X))**0.5

# def rollDie():
#     return random.choice([1,2,3,4,5,6])

def rollDie():              #make 5 easier appear than 2
    return random.choice([1,1,2,3,3,4,4,5,5,5,6,6])


class CrapsGame(object):
    def __init__(self):
        self.passWins,self.passLosses=(0,0)
        self.dpWins,self.dpLosses,self.dpPushes=(0,0,0)

##此处注意，playHand的调用结果与循环次数无关，只与循环退出的条件有关
    def playHand(self):
        pointDict={4:1/3.0,5:2/5.0,6:5/11.0,8:5/11.0,9:2/5.0,10:1/3.0}
        throw=rollDie()+rollDie()
        if throw==7 or throw==11:
            self.passWins+=1
            self.dpLosses+=1
        elif throw==2 or throw==3 or throw==12:
            self.passLosses+=1
            if throw==12:
                self.dpPushes+=1
            else:
                self.dpWins+=1
        else:
            if random.random()<=pointDict[throw]: #掷出7之前掷出该点
                self.passWins+=1
                self.dpLosses+=1
            else:
                self.passLosses+=1
                self.dpWins+=1

    def passResults(self):
        return(self.passWins,self.passLosses)

    def dpResults(self):
        return(self.dpWins,self.dpLosses,self.dpPushes)

#模拟双骰子游戏
def crapsSim(handsPerGame,numGames):
    '''assume handsPerGame and numGames are int
       play every time there handsPerGame times games,and have numGames times to print the result'''
    games=[]

    #play numGames times games
    for t in xrange(numGames):
        c=CrapsGame()
        for i in xrange(handsPerGame):
            c.playHand()
        games.append(c)

    #generate the statistic result of every game
    pROIPerGame,dpROIPerGame=[],[]
    for g in games:
        wins,losses=g.passResults()
        pROIPerGame.append((wins-losses)/float(handsPerGame))
        wins,losses,pushes=g.dpResults()
        dpROIPerGame.append((wins-losses)/float(handsPerGame))


    #generate and print summary
    meanROI=str(round((100.0*sum(pROIPerGame)/numGames),4))+'%'
    sigma=str(round(100.0*stdDev(pROIPerGame),4))+'%'
    print 'Pass:','Mean ROI=',meanROI,'std.Dev.=',sigma
    meanROI=str(round((100.0*sum(dpROIPerGame)/numGames),4))+'%'
    sigma=str(round(100.0*stdDev(dpROIPerGame),4))+'%'
    print 'Don\'t Pass:','Mean ROI=',meanROI,'std.Dev.=',sigma


# crapsSim(20,10)
crapsSim(10000,10)
# crapsSim(20,10000)
