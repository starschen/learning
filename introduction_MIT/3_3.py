#encoding:utf8
#3.3近似解和二分查找

# x=25
# epsilon=0.01
# step=epsilon**2
# numGuesses=0
# ans=0.0
# while abs(ans**2-x)>=epsilon and ans<=x:
#     ans+=step
#     numGuesses+=1
# print 'numGuesses=',numGuesses
# if abs(ans**2-x)>=epsilon:
#     print 'Failed on square root of',x
# else:
#     print ans,'is close to square root of',x


# x=25
# epsilon=0.01
# numGuesses=0
# low=0.0
# high=max(0.0,x)
# ans=(high+low)/2.0
# while abs(ans**2-x)>=epsilon:
#     print 'low=',low,'high=',high,'ans=',ans
#     numGuesses+=1
#     if ans**2<x:
#         low=ans
#     else:
#         high=ans
#     ans=(high+low)/2.0
# print 'numGuesses=',numGuesses
# print ans,'is close to square root of',x


x=-27
epsilon=0.01
numGuesses=0
low=min(0.0,x)
high=max(0.0,x)
ans=(high+low)/2.0
while abs(ans**3-x)>=epsilon:
    print 'low=',low,'high=',high,'ans=',ans
    numGuesses+=1
    if ans**3<x:
        low=ans
    else:
        high=ans
    ans=(high+low)/2.0
print 'numGuesses=',numGuesses
print ans,'is close to cube root of',x
