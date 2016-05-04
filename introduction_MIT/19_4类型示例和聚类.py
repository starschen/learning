#encoding:utf8
#19_4类型示例和聚类.py
import pylab
#闵可夫斯基距离
def minkowskiDist(v1,v2,p):
    '''假设v1和v2是等长的数字数组，返回顺序为p时v1和v2的距离'''
    dist=0.0
    for i in range(len(v1)):
        dist+=abs(v1[i]-v2[i])**p
    return dist**(1.0/p)

#Example类
class Example(object):

    def __init__(self,name,features,label=None):
        #假设features是数字列表
        self.name=name
        self.features=features
        self.label=label

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self,other):
        return minkowskiDist(self.features,other.getFeatures(),2)

    def __str__(self):
        return self.name+':'+str(self.features)+':'+str(self.label)
#Cluster类
class Cluster(object):

    def __init__(self,examples,exampleType):
        '''假设examples是 exampleType类型的实例列表'''
        self.examples=examples
        self.exampleType=exampleType
        self.centroid=self.computeCentroid()#computeCentroid质心

    def update(self,examples):
        '''用新实例替换簇中的实例，返回质心的改变量'''
        oldCentroid=self.centroid
        self.examples=examples
        if len(examples)>0:
            self.centroid=self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0

    def members(self):
        for e in self.examples:
            yield e

    def size(self):
        return len(self.examples)

    def getCentroid(self):
        return self.centroid

    def computeCentroid(self):
        dim=self.examples[0].dimensionality()
        totVals=pylab.array([0.0]*dim)
        for e in self.examples:
            totVals+=e.getFeatures()
        centroid=self.exampleType('centroid',totVals/float(len(self.examples)))
        return centroid

    def variance(self):
        totDist=0.0
        for e in self.examples:
            totDist+=(e.distance(self.centroid))**2
        return totDist**0.5

    def __str__(self):
        names=[]
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result='Cluster with centroid'+str(self.centroid.getFeatures())+'contains:\n'
        for e in names:
            result=result+e+','
        return result[:-2]
