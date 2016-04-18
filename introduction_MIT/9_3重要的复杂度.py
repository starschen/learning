#encoding:utf8
#9.3一些重要的复杂度
#对数复杂度
def int2str(i):
    digits='0123456789'
    if i==0:
        return '0'
    result=''
    while i>0:
        result=digits[i%10]+result
        i=i//10
    return result

# print int2str(0)
# print type(int2str(123))

def adddigits(n):
        stringrep=int2str(n)
        val=0
        for c in stringrep:
            val+=int(c)
        return val

# print adddigits(123)

#线性复杂度
def adddigits(s):
    '''assume s is string,return sum(int(s))'''
    val=0
    for c in s:
        val+=int(c)
    return val

# print adddigits('12345')

def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

#多项式复杂度
def issubset(l1,l2):
    for e1 in l1:
        matched=False
        for e2 in l2:
            if e1==e2:
                matched=True
                break
        if not matched:
            return False
    return True

# print issubset([1,2,3],[2,3])
# print issubset([1,2,3],[1,2,3])

def intersect(l1,l2):
    tmp=[]
    for e1 in l1:
        for e2 in l2:
            if e1==e2:
                tmp.append(e1)
    result=[]
    for e in tmp:
        if e not in result:
            result.append(e)
    return result

# print intersect([1,2,3],[2,3,4])
# print intersect([1],[2,3,4])

#指数复杂度
def getbinaryrep(n,numdigits):
    result=''
    while n>0:
        result=str(n%2)+result
        n=n//2
    if len(result)>numdigits:
        raise ValueError('not enough digits')
    for i in range(numdigits-len(result)):
        result='0'+result
    return result

def genpowerset(l):
    powerset=[]
    for i in range(2**len(l)):
        binstr=getbinaryrep(i,len(l))
        subset=[]
        for j in range(len(l)):
            if binstr[j]=='1':
                subset.append(l[j])
        powerset.append(subset)
    return powerset

print genpowerset(['a','b'])
