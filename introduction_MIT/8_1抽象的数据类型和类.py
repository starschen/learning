#encoding:utf8
#8.1抽象的数据类型和类

class IntSet(object):
    """IntSet是一组整数"""
    #实现（而非抽象）的信息
    #值存储在列表self.vals中
    #每个值只出现一次

    def __init__(self):
        """创建一个空的整数列表"""
        self.vals=[]

    def insert(self,e):
        """假定e是整数，把e插入self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self,e):
        """假定e是整数
           如果e在self中返回True,否则返回False"""
        return e in self.vals

    def remove(self,e):
        """假定e是整数，从self中删除e
           如果e不在self中触发ValueError异常"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+'not found')

    def getMember(self):
        """返回包含self中元素的列表。
           元素的顺序无法假设。"""
        return self.vals[:]

    def __str__(self):
        """返回self的字符串形式"""
        self.vals.sort()
        result=''
        for e in self.vals:
            result=result+str(e)+','
        return '{' + result[:-1]+ '}'


# s=IntSet()
# s.insert(3)
# print s.member(3)


#8.1.2用类记录学生和老师

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

me=Person('Michael Guttag')
him=Person('Barack Hussein Obama')
her=Person('Madonna')
# print him.getLastName()
# him.setBirthday(datetime.date(1961,8,4))
# her.setBirthday(datetime.date(1958,8,16))
# print him.getName(),'is',him.getAge(),'days old'

pList=[me,him,her]
for p in pList:
    print p
pList.sort()
for p in pList:
    print p
