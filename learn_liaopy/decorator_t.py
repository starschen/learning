import functools
#1
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print 'begin call %s():' %func.__name__
#         func(*args,**kw)
#         print '%s() call end' %func.__name__
#     return wrapper
#
# @log
# def now():
#     print '2016-8-16'
#
# now()

#2
def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*args,**kw):
            print 'call %s():' %text.__name__
            return text(*args,**kw)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print '%s,%s():' %(text,func.__name__)
                return func(*args,**kw)
            return wrapper
        return decorator

@log
def now1():
    print 'doing 1...'

@log('text')
def now2():
    print 'doing 2...'

now1()
now2()
