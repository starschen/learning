# #encoding:utf8
from functools import reduce
# #1
# def fn(x,y):
#     return x*10+y
#
# def char2num(s):
#     return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#
# print reduce(fn,map(char2num,'13579'))
#
# #2
# def str2int(s):
#     def fn(x,y):
#         return x*10+y
#     def char2num(s):
#         return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#     return reduce(fn,map(char2num,s))
#
# print str2int('13579')
#
# #3
# def char2num(s):
#     return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#
# def str2int(s):
#     return reduce(lambda x,y:x*10+y,map(char2num,s))
#
# print str2int('13579')
#
# #4
# def normalize(name):
#     return name.capitalize()
#
# l1=['adam','LISA','barT']
# print list(map(normalize,l1))
#
# #5
# def fn(x,y):
#     return x*y
#
# def prod(L):
#     return reduce(fn,L)
#
# print '3*5*7*9=',prod([3,5,7,9])
#
# #6
# def char2num(s):
#     return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#
# def fn(x,y):
#     return x*10+y
#
# def str2float(s):
#     if s.find('.')== -1:
#         return reduce(fn,map(char2num,s))
#     else:
#         return reduce(fn,(map(char2num,s[:s.find('.')])))+reduce(fn,(map(char2num,s[s.find('.')+1:])))/10.0**len(s.split('.')[1])
#     return reduce(fn,map(char2num,s))
#
# print str2float('0.456')
#
# #7
# def char2num(s):
#      return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#
# def str2float(s):
#     if s.find('.')==0:
#         return reduce(lambda x,y:x*10+y,map(char2num,s))
#     else:
#         return reduce(lambda x,y:x*10+y,map(char2num,s[:s.find('.')]))+reduce(lambda x,y:x/10.0+y/100.0,map(char2num,s[s.find('.')+1:]))
#
# print str2float('123.456')
#
# def str2float(s):
#     def char2int(a):
#             return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}[a]
#     if s.find('.')==0:
#         return reduce(lambda x,y:x*10+y,map(char2int,[x for x in s.split('.')[1]]))/10**len(s.split('.')[1])
#     else:
#         return reduce(lambda x,y:x*10+y,map(char2int,[x for x in s.split('.')[0]]))+reduce(lambda x,y:x*10+y,map(char2int,[x for x in s.split('.')[1]]))/10**len(s.split('.')[1])
#
# print('测试',str2float('.1232'))
# print('测试',str2float('00.1232'))
# print('测试',str2float('00.123200'))
#
# #8
# def is_odd(n):
#     return n%2==1
#
# print list(filter(is_odd,[1,2,4,5,6,9,19,20]))
#
# def not_empty(s):
#     return s and s.strip()
#
# print list(filter(not_empty,['A','B',None,'C','']))
#
# #9
from itertools import ifilter
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=_odd_iter()
    while True:
        n=next(it)
        yield n
        it=ifilter(_not_divisible(n),it)

for n in primes():
    if n <50:
        print(n)
    else:
        break
#
# #10
# def is_pallindrome(n):
#     s=list(str(n))
#     i=0
#     for s[i] in s:
#         if s[i]==s[-i-1]:
#             return True
#         else:
#             return False
#         i=i+1
#
# print list(filter(is_pallindrome,range(1,1000)))
#
# def is_pallindrome(n):
#     return str(n)==str(n)[::-1]
# print list(filter(is_pallindrome,range(1,1000)))
#
# ##11
# L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#
# def by_name(t):
#     return t[0]
#
# def by_score(t):
#     return t[1]
#
# print 'by_name:',sorted(L,key=by_name)
# print 'by_score:',sorted(L,key=by_score,reverse=True)
