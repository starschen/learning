class Student(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'Student object (name:%s)' %self.name

# print Student('Emma')
s=Student('Emma')
# print s

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a

# for n in Fib():
#     print n
# print Fib()[5]

class Fib2(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a

f=Fib2()
# for i in range(10):
#     print f[i]
# print Fib2(10)[5:9]

class Fib3(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            a,b=1,1
            l=[]
            for x in range(stop):
                if x>=start:
                    l.append(a)
                a,b=b,a+b
            return l

# f=Fib3()
# print f[0:5]
# print f[:10]
# print f[:10:2]

class Student2(object):
    def __init__(self):
        self.name='Michael'

    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda:25
        raise AttributeError('\'Student2\' object has no attribute \'%s\'' % attr)

# s=Student2()
# print s.name
# print s.score
# print s.age()
# print s.abc

class Chain(object):

    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))

    def __str__(self):
        return self._path


# print Chain().status.user.timeline.list

class Student3(object):
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print 'My name is %s.' %self.name

# s=Student3('Emma')
# s()

print callable(Student3)
print callable(max)
print callable([1,2,3])
print callable(None)
print callable('string')
