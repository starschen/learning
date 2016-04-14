#encoding:utf8
#8.2继承

#8-1在person类
import datetime

class Person(object):

    def __init__(self,name):
        """创建一个人"""
        self.name=name
        try:
            lastBlank=name.rindex(' ')
            self.lastName=name[lastBlank+1:]
        except:
            self.lastName=name
        self.birthday=None

    def getName(self):
        """返回这个人的姓名"""
        return self.name

    def getLastName(self):
        """返回这个人的姓"""
        return self.lastName

    def setBirthday(self,birthDate):
        """假定birthDate是datetime.date类型
           把birthDate设置为这个人的生日"""
        self.birthday=birthDate

    def getAge(self):
        """返回这个人当前的年龄对应的天数"""
        if self.birthday==None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        """如果这个人的名字字典小于另一个人的名字返回True,否则返回False"""
        if self.lastName==other.lastName:
            return self.name<other.name
        return self.lastName<other.lastName

    def __str__(self):
        """返回这个人的名字"""
        return self.name

#8.2
class MITPerson(Person):

    nextIdNum=0 #身份证号

    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum=MITPerson.nextIdNum
        MITPerson.nextIdNum+=1

    def getIdNum(self):
        return self.idNum

    def __lt__(self,other):
        return self.idNum<other.idNum

    def isStudent(self):
        # return isinstance(self,Student)
        return type(self)==Grad or type(self)==UG

# p1=MITPerson('Barbara Beaver')
# print str(p1)+'\'s id number is ' +str(p1.getIdNum())

p1=MITPerson('Mark Guttag')
p2=MITPerson('Billy Bob Beaver')
p3=MITPerson('Billy Bob Beaver')
p4=Person('Bill Bob Beaver')

# print 'p1<p2=',p1<p2
# print 'p3<p2=',p3<p2
# print 'p4<p1=',p4<p1

#8.2.1多层继承
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

class TransferStudent(Student):

    def __init__(self,name,fromSchool):
        MITPerson.__init__(self,name)
        self.fromSchool=fromSchool

    def getOldSchool(self):
        return self.fromSchool


p5=Grad('Buzz Aldrin')
p6=UG('Billy Beaver',1984)
# print p5,'is a graduate student is',type(p5)==Grad
# print p5,'is an undergraduate student is',type(p5)==UG

print p5,'is a student is',p5.isStudent()
print p6,'is a student is',p6.isStudent()
print p3,'is a student is',p3.isStudent()
