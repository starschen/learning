#encoding:utf8
#3.1穷举法
#寻找完全立方数的立方根
# x=int(raw_input('Enter an integer: '))
# ans=0
# while ans**3<abs(x):
#     ans=ans+1
# if ans**3!=abs(x):
#     print x,'is not a perfect cube'
# elif x<0:
#     ans=-ans
# else:
#     print 'Cube root of ',x,' is ',ans


# max=int(raw_input('Enter a positive integer: '))
# i=0
# while i<max:
#     i=i+1
# print i


##编写一个程序，要求用户输入一个整数并输出两个整数root和pwr，满足0<pwr<6并且root**pwr和用户输入的整数相等。
##如果不存在满足条件的整数对，输出一条信息来说明。
##如何让root和pwr自已加自己的？
#咋还是不对呢？5.5
m=int(raw_input('Enter an integer: '))
for pwr in range(1,6):
    for root in range(abs(m)+1):
        if root**pwr>abs(m):
            break


if root**pwr!=abs(m):
    print 'not exist root pwr'
elif root<0:
    root=-root
else:
    print 'root= ',root,'pwr= ',pwr
