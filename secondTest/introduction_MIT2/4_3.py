#encoding:utf8
def facI(n):
    result=1
    while n>0:
        result=result*n
        n=n-1
    return result

def facR(n):
    if n==1:
        return n
    else:
        return n*facR(n-1)

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def testFib(n):
    for i in range(n+1):
        print 'fib of',i,'=',fib(i)


def isPalindrome(s):
    def toChar(s):
        s=s.lower()
        letters=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters=letters+c
        return letters

    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))
