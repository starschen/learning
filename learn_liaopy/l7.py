#encoding:utf8

##1
# def log(func):
#     def wrapper(*args,**kw):
#         print 'call %s():' %func.__name__
#         return func(*args,**kw)
#     return wrapper

# @log
# def now():
#     print '2013-1-3'

# now=log(now)

##2
# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print '%s %s():' %(text,func.__name__)
#             return func(*args,**kw)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print '2013-1-3'

##3
import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print 'call %s():' %func.__name__
#         return func(*args,**kw)
#     return wrapper
#
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print '%s %s():' %(text,func.__name__)
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# ##4无参数装饰器－包装无参数函数
# def decorator(func):
#     print 'hello'
#     return func
#
# @decorator
# def foo():
#     pass   #foo=decorator(foo)
#
# foo()

##5无参数装饰器－包装带参数函数
# def decorator_func_args(func):
#     def handle_args(*args,**kwargs):
#         print 'begin'
#         func(*args,**kwargs)
#         print 'end'
#     return handle_args
#
# @decorator_func_args
# def foo2(a,b=2):
#     print a,b    #foo2=decorator_func_args(foo2)
#
# foo2(1,3)

##6带参数装饰器－包装无参数函数
# def decorator_with_params(arg_of_decorator):  #这里是装饰器参数
#     print arg_of_decorator
#     #最终被返回的函数
#     def newDecorator(func):
#         print func
#         return func
#     return newDecorator
#
# @decorator_with_params('deco_args')
# def foo3():
#     pass          #foo3=decorator_with_params(arg_of_decorator)(foo3)
#
# foo3()
#
# #7#带参数装饰器－包装带参数函数
# def decorator_with_params_and_func_args(arg_of_decorator):
#     def handle_func(func):
#         def handle_args(*args,**kwargs):
#             print "begin"
#             func(*args,**kwargs)
#             print "end"
#             print arg_of_decorator,func,args,kwargs
#         return handle_args
#     return handle_func
#
# @decorator_with_params_and_func_args('123')
# def foo4(a,b=2):
#     print "Content"
#
# foo4(1,b=3)

##8
# def log(function):
#     def wrapper(*args,**kwargs):
#         print 'before function[%s()run]' %function.__name__
#         rst=function(*args,**kwargs)
#         print 'after function[%s()run]' %function.__name__
#         return rst
#     return wrapper
#
# @log
# def func():
#     print '函数运行'
#
# if '__main__'==__name__:
#     func()

##9
# def log(text=''):
#     def decorator(function):
#         @functools.wraps(function)
#         def wrapper(*args,**kwargs):
#             print 'before function [%s()] run,text:[%s]' %(function.__name__,text)
#             rst=function(*args,**kwargs)
#             print 'after function [%s()] run,text:[%s]' %(function.__name__,text)
#             return rst
#         return wrapper
#     return decorator
#
# @log('log text')
# def func():
#     print '函数运行'
#
# if '__main__'==__name__:
#     func()

##9廖装饰器习题1
import functools

# def log(func):
#     def wrapper(*args,**kwargs):
#         print 'begin call'
#         rst=func(*args,**kwargs)
#         print 'end call'
#         return rst
#     return wrapper
#
# @log
# def func():
#     print 'func run'

# def log(func):
#     print 'begin call'
#     rst=func()
#     print 'end call'
#     return rst
#
#
# @log
# def func():
#     print 'func run'

##10廖装饰器习题1
def log(text):
    if isinstance(text,(str,int,float)):
        def decorator(func):
            def wrapper(*args,**kw):
                print('%s %s():'%(text,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator
    else:
        func=text
        def wrapper(*args,**kw):
            print ('call %s():'%func.__name__)
            return func(*args,**kw)
        return wrapper

@log
def f():
    print '无添加额外日志成功'

@log('execute')
def f2():
    print '添加额外日志成功'
