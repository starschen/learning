#encoding:utf8
#3.5牛顿－拉夫逊方法

##用牛顿－拉夫逊方法 寻找平方根
#寻找x，满足x**2-24在epsilon和0之间
# epsilon=0.01
# k=25.0
# guess=k/2.0
# count=0
# while abs(guess*guess-k)>=epsilon:
#     guess=guess-(((guess**2)-k)/(2*guess))
#     count+=1
# print 'Square root of',k,'is about',guess
# print count



x=25
epsilon=0.01
numGuesses=0
low=0.0
high=max(0.0,x)
ans=(high+low)/2.0
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
