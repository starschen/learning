#!/usr/bin/env python
#encoding:utf8

# 'a test module'
#
# __author__='Emma Chen'
#
# import sys
# def test():
#     args=sys.argv
#     if len(args)==1:
#         print 'Hello,wolrd!'
#     elif len(args)==2:
#         print 'Hello,%s!' %args[1]
#     else:
#         print 'Too many arguments!'
#
# if __name__=='__main__':
#     test()
#
# #别名
# try:
#     import cStringIO as StringIO
# except ImportError:
#     import StringIO
#
# try:
#     import json
# except ImportError:
#     import simplejson as json

#作用域
def _private_1(name):
    return 'Hello,%s' %name

def _private_2(name):
    return 'Hi,%s' %name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)

print greeting('A')
print greeting('Emma')
