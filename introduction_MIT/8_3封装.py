#encoding:utf8
#8.3封装

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


#8.3
class Grades(object):
    """学生到成绩列表的映射关系"""
    def __init__(self):
        """创建一个空的成绩册"""
        self.students=[]
        self.grades={}
        self.isSorted=True

    def addStudent(self,student):
        """假定student类型为Student
           把student添加到成绩册"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()]=[]
        self.isSorted=False

    def addGrade(self,student,grade):
        """假定成绩是浮点数
           把成绩添加到对应学生的成绩册上"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self,student):
        """返回学生的成绩列表"""
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """返回成绩册中学生的列表"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted=True
        return self.students[:]

# allStudents=course1.getStudents()
# allStudents.extend(course2.getStudents())

def gradeReport(course):
    """假定course类型为Grades"""
    report=''
    for s in course.getStudents():
        tot=0.0
        numGrades=0
        for g in course.getGrades(s):
            tot+=g
            numGrades+=1
        try:
            average=tot/numGrades
            report=report+'\n'+str(s)+'\'s mean grade is '+str(average)
        except ZeroDivisionError:
            report =report+'\n'+str(s)+'has no grade'
    return report

ug1=UG('Jane Doe',2014)
ug2=UG('John Doe',2015)
ug3=UG('David Henry',2003)
g1=Grad('Billy Buckner')
g2=Grad('Bucky f. Dent')
sixHundred=Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
for s in sixHundred.getStudents():
    sixHundred.addGrade(s,75)
sixHundred.addGrade(g1,25)
sixHundred.addGrade(g2,100)
sixHundred.addStudent(ug3)
print gradeReport(sixHundred)

#8.3.1生成器
def getStudents(self):
    """返回成绩册中学生的列表"""
    if not self.isSorted:
        self.student.sort()
        self.isSorted=True
    for s in self.students:
        yield s
