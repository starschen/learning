#encoding:utf8
#4.1函数和作用域

#4.1.2关键字参数和默认值
# def printName(firstName,lastName,reverse):
#     if reverse:
#         print lastName+ ','+firstName
#     else:
#         print firstName,lastName
#
# printName('Olga','Puchmajerova',False)
# printName('Olga','Puchmajerova',reverse=False)
# printName('Olga',lastName='Puchmajerova',reverse=False)
# printName(lastName='Puchmajerova',firstName='Olga',reverse=False)


#4.1.3作用域
# def f(x):
#     y=1
#     x=x+y
#     print 'x=',x
#     return x
#
# x=3
# y=2
# z=f(x)
# print 'z=',z
# print 'x=',x
# print 'y=',y

# def f(x):  #x=3
#     def g():
#         x='abc'
#         print 'x=',x
#     def h():
#         z=x
#         print 'z=',z
#     x=x+1
#     print 'x=',x
#     h()
#     g()
#     print 'x=',x
#     return g
# x=3
# z=f(x)
# print 'x=',x
# print 'z=',z
# z()

def f():
    print x

def g():
    print x  #出错
    x=1

x=3
f()
x=3
g()
