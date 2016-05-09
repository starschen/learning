#encoding:utf8

def findDivisors(n1,n2):
    divisors=()
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            divisors=divisors+(i,)
    return divisors

divisors=findDivisors(20,200)
# print divisors
total=0
for d in divisors:
    total+=d
# print total

def findExtremeDivisors(n1,n2):
    divisors=()
    minVal,maxVal=None,None
    for i in range(2,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            if minVal==None or i<minVal:
                minVal=i
            if maxVal==None or i >maxVal:
                maxVal=i
    return (minVal,maxVal)

# minVal,maxVal=findExtremeDivisors(100,200)
# print 'minVal=',minVal
# print 'maxVal=',maxVal
print findExtremeDivisors(100,200)
