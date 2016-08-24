class Student(object):
    __slots__=('name','age')

s=Student()
s.name='Michael'
# print s.name
s.age=25
# s.score=99

class GraduateStudent(Student):
    pass

g=GraduateStudent()
g.score=999

# def set_age(self,age):
#     self.age=age

# from types import MethodType
# s.set_age=MethodType(set_age,s,Student)
# s.set_age(25)
# # print s.age
#
# s2=Student()
# # s2.set_age(25)
# # print s2.age
#
# def set_score(self,score):
#     self.score=score
#
# Student.set_score=MethodType(set_score,None,Student)
# s.set_score(100)
# print s.score
#
# s2.set_score(99)
# print s2.score
