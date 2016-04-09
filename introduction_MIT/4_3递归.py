#encoding:utf8
#4.3递归
# def factI(n):
#     '''Assumes that n is an int>o
#        Returns n!'''
#     result=1
#     while n>1:
#         result=result*n
#         n-=1
#     return result
#
# def factR(n):
#     '''Assumes that n is an int>0
#        returns n!'''
#     if n==1:
#         return n
#     else:
#         return n*factr(n-1)

#4.3.1斐波那契数
# def fib(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# def  testFib(n):
#     for i in range(n+1):
#         print 'fib of ',i,'=',fib(i)
#
# testFib(24)


#4.3.2回文和分治
def isPalindrome(s):
    '''假定S是字符串
       如果S是回文字符串返回True，否则返回False。
       忽略标点符号、空格和大小写。'''
    def toChars(s):
        s=s.lower()
        letters=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters=letters+c
        return letters

    def isPal(s):
        print ' isPal called with',s
        if len(s)<=1:
            print 'About to return True from base case'
            return True
        else:
            answer= s[0]==s[-1] and isPal(s[1:-1])
            print 'About to return',answer,'for',s
            return answer

    return isPal(toChars(s))

def testIsPalindrome():
    print 'Try dogGod'
    print isPalindrome('dogGod')
    print 'Try doGood'
    print isPalindrome('doGood')

testIsPalindrome()
