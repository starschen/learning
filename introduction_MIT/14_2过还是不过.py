#encoding:utf8
#14.2过还是不过
#CrapsGame类
#CrapsGame类的实例会记录游戏开始之后过线和不过线的情况，观察者passResults和dpResults会返回对应的值。
#playHand方法会模拟一手游戏，playHand中的代码几科就是直接用算法描述上述的游戏规则。
#
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

    def playHand(self):
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
            point=throw
            while True:
                throw=rollDie()+rollDie()
                if throw==point:
                    self.passWins+=1
                    self.dpLosses+=1
                    break
                elif throw==7:
                    self.passLosses+=1
                    self.dpWins+=1
                    break

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
