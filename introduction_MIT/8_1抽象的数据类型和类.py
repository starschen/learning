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


s=IntSet()
s.insert(3)
print s.member(3)
