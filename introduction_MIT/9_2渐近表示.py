#encoding:utf8
#9.2渐近表示

def f(x):
    '''assume x is int'''
    ans=0
    for i in range(1000):
        ans+=1
    print 'Number of additions so far',ans

    for i in range(x):
        ans+=1
    print 'Number of additions so far',ans

    for i in range(x):
        for j in range(x):
            ans+=1
            ans+=1
    print 'Number of additons so far',ans
    return ans

print f(10)
