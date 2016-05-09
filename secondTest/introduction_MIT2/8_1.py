#encoding:utf8

class Intset(object):
    def __init__(self):
        self.vals=[]

    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self,e):
        return e in self.vals

    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+'not an integer')

    def getMember(self):
        return self.vals[:]

    def __str__(self):
        self.vals.sort()
        result=''
        for e in self.vals:
            result=result+str(e)+','
        return '{'+result[:-1]+'}'

# s=Intset()
# s.insert(3)
# s.insert(4)
# print s

import datetime
class Person(object):

    def __init__(self,name):
        self.name=name
        try:
            lastBlank=name.rindex(' ')
            self.lastName=name[lastBlank+1:]
        except:
            self.lastName=name
        self.birthday=None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self,birthDate):
        self.birthday=birthDate

    def getAge(self):
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        if self.lastName==other.lastName:
            return self.name<other.name
        return  self.lastName<other.lastName

    def __str__(self):
        return self.name

# me=Person('Emma chen')
# him=Person('Beast bao')
# her=Person('Some one')
# print him.getLastName()
# him.setBirthday(datetime.date(1987,6,1))
# her.setBirthday(datetime.date(1989,6,1))
# print him.getName(),'is',him.getAge(),'days old'

class MITPerson(Person):

    nextIdNum=0

    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum=MITPerson.nextIdNum
        MITPerson.nextIdNum+=1

    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum<other.idNum
