#encoding:utf8

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

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

def isStudent(self):
    return isinstance(self,Student)

class TransferStudent(Student):
    def __init__(self,name,fromSchool):
        MITPerson.__init__(self,name)
        self.fromSchool=fromSchool

    def getOldSchool(self):
        return self.fromSchool
