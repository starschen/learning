#encoding:utf8
#3.2 for 循环

# x=4
# for i in range(0,x):
#     print i

# x=4
# for i in range(0,x):
#     print i
#     x=5
#
# x=4
# for i in range(x):
#     for j in range(x):
#         print j
#         x=2

#寻找完全立方数的立方根
# x=int(raw_input('Enter an integer: '))
# for ans in range(abs(x)+1):
#     if ans**3>=abs(x):
#         break
# if ans**3!=abs(x):
#     print x,'is not a pergect cube'
# elif x<0:
#     ans=-ans
# else:
#     print 'Cube root of',x,'is',ans


# total=0
# for c in '123456789':
#     total=total+int(c)
# print total

s=raw_input().split(',')
s=map(float,s)
print sum(s)
