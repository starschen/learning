#encoding:utf8
#4.4全局变量

def fib(x):
    '''假定x是正整数
       返回第x个斐波那契数'''
    global numFibCalls
    numFibCalls+=1
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls=0
        print 'fib of',i,'=',fib(i)
        print 'fib called',numFibCalls,'times.'

testFib(10)
