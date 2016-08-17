import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print 'call %s():' %func.__name__
        return func(*args,**kw)
    return wrapper


#带参数的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():' %(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return decorator
