#encoding:utf8
# x=int(raw_input())
# epsilon=0.01
# numGuesses=0
# low=min(0.0,x)
# high=max(0.0,x)
# ans=(low+high)/2.0
# while abs(ans**3-x)>=epsilon:
#     print 'low=',low,'high=',high,'ans=',ans
#     numGuesses+=1
#     if ans**3<x:
#         low=ans
#     else:
#         high=ans
#     ans=(high+low)/2.0
# print 'numGuesses=',numGuesses
# print ans,'is close to square root of',x


x=int(raw_input())
epsilon=0.01
numGuesses=0
low=min(0.0,x)
high=max(0.0,x)
ans=(low+high)/2.0
while abs(ans**2-x)>=epsilon:
    print 'low=',low,'high=',high,'ans=',ans
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(high+low)/2.0
print 'numGuesses=',numGuesses
print ans,'is close to square root of',x
