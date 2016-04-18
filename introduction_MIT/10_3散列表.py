#encoding:utf8
#10.3散列表

#4.18这段段码运行结果不对，暂时还没找到原因。
class intdict(object):
    '''the dict that keys are int'''

    def __init__(self,numbuckets):
        self.buckets=[]
        self.numbuckets=numbuckets
        for i in range(numbuckets):
            self.buckets.append([])

    def addentry(self,dictkey,dictval):
        hashbucket=self.buckets[dictkey%self.numbuckets]
        print self.dictkey,self.numbuckets
        for i in range(len(hashbucket)):
            if hashbucket[i][0]==dictkey:
                hashbucket[i]=(dictkey,dictval)
                return hashbucket.append(dictkey,dictval)

    def getvalue(self,dictkey):
        hashbucket=self.buckets[dictkey%self.numbuckets]
        for e in hashbucket:
            if e[0]==dictkey:
                return e[1]
        return None

    def __str__(self):
        result='{'
        for b in self.buckets:
            for e in b:
                result=result+str(e[0])+':'+str(e[1])+','
        return result[:-1]+'}'

import random
d=intdict(29)
for i in range(20):
    key=random.randint(0,10**5)
    d.addentry(key,i)
print 'The value of the intdict is:'
print d
print '\n','THe buckets are:'
for hashbucket in d.buckets:
    print '   ',hashbucket
