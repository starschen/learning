#encoding:utf8
#19_5K-means聚类.py
#K-means聚类目标是把一组实例分割成k个簇，满足：
#1）每个实例到处在质心距离实例质心最近的簇中，并且
#2）所有族的差异总和最小
#贪心算法
#随机选择k个实例作为初始质心
#无限循环：
#1）把每个实例分配给最近的抟，从而创建k个簇；
#2）通过平均每个簇中的实例来得到k个新质心；
#3）如果所有质心都和计算之前相同，返回当前的簇集合。
import pylab
import random
#19_4
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

#19_5K-means
#K-means聚类
def kmeans(examples,exampleType,k,verbose):
    '''假设examples和exampleType类型的实例列表，k是正整数， verbose是布尔值
       返回包含k个簇的列表。
       如果 verbose为 True，输出 K-means每次迭代的结果'''
    #生成k个随机初始质心
    initialCentroids=random.sample(examples,k)

    #每个质心创建一个单例簇
    clusters=[]
    for e in initialCentroids:
        clusters.append(Cluster([e],exampleType))

    #不断迭代，直到质心不变
    converged=False
    numIterations=0
    while not converged:
        numIterations+=1
        #创建一个列表，包含K个空列表
        newClusters=[]
        for i in range(k):
            newClusters.append([])

        #每个实例关联到最近的质心
        for e in examples:
            #找到离e最近的质心
            smallestDistance=e.distance(clusters[0].getCentroid())
            index=0
            for i in range(1,k):
                distance=e.distance(clusters[0].getCentroid())
                if distance<smallestDistance:
                    smallestDistance=distance
                    index=i
            #把e添加到对庆簇的实例列表中
            newClusters[index].append(e)

        #更新所有族、判断质心是否改变
        converged=True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i])>0.0:
                converged=False
        if verbose:
            print 'Iteration #'+str(numIterations)
            for c in clusters:
                print c
            print '' #add blank line
    return clusters

#寻找最佳K-means聚类
def dissimilarity(clusters):
    totDist=0.0
    for c in clusters:
        totDist+=c.variance()
    return totDist

def trykmeans(examples,exampleType,numClusters,numTrials,verbose=False):
    '''调用kmeans numTrials次并返回差异总和最小的结果'''
    best=kmeans(examples,exampleType,numClusters,verbose)
    minDissimilarity=dissimilarity(best)
    for trial in range(1,numTrials):
        clusters=kmeans(examples,exampleType,numClusters,verbose)
        currDissimilarity=dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best=clusters
            minDissimilarity=currDissimilarity
    return best
