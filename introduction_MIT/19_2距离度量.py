#encoding:utf8
#19_2距离度量.py
import pylab
#闵可夫斯基距离
def minkowskiDist(v1,v2,p):
    '''假设v1和v2是等长的数字数组，返回顺序为p时v1和v2的距离'''
    dist=0.0
    for i in range(len(v1)):
        dist+=abs(v1[i]-v2[i])**p
    return dist**(1.0/p)

#Animal类，通过动物特征向量的欧氏距离定义出两种动物的距离
class Animal(object):
    def __init__(self,name,features):
        '''假设name是字符串， features是数字列表'''
        self.name=name
        self.features=pylab.array(features)

    def getName(self):
        return self.name

    def getFeatures(self):
        return self.features

    def distance(self,other):
        '''假设other是一个动物， 返回self和other特征向量的欧氏距离'''
        return minkowskiDist(self.getFeatures(),other.getFeatures(),2)

#生成表格，显示每两个动物之间的距离。对一组动物进行对比并将结果展示在表格中
def compareAnimals(animals,precision):
    '''假设animals是动物列表， precision是大于等于0的整数，生成一个表格，包含任意两个动物之间的欧氏距离'''
    #生成表格的行与列
    columnLabels=[]
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels=columnLabels[:]
    tableVals=[]
    #计算动物之间的距离
    #循环每行
    for a1 in animals:
        row=[]
        #循环每列
        for a2 in animals:
            if a1==a2:
                row.append('--')
            else:
                distance=a1.distance(a2)
                row.append(str(round(distance,precision)))
        tableVals.append(row)
    #生成表格
    table=pylab.table(rowLabels=rowLabels,
                      colLabels=columnLabels,
                      cellText=tableVals,
                      cellLoc='center',
                      loc='center',
                      colWidths=[0.2]*len(animals))
    table.scale(1,2.5)
    pylab.axis('off') #不显示x轴和y轴
    pylab.savefig('distances')

rattlesnake=Animal('rattlesnake',[1,1,1,1,0])
boa=Animal('boa\nconstrictor',[0,1,0,1,0])
dartFrog=Animal('dart frog',[1,0,1,0,1])
animals=[rattlesnake,boa,dartFrog]
alligator=Animal('alligator',[1,1,0,1,1])
animals.append(alligator)
compareAnimals(animals,3)
