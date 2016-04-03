#encoding:utf8
#1091 A+B for Input-Output Practice(III)

##1下面这段有问题
# l=[]
# n=raw_input().split(' ')
# n=map(int,n)
# while n<>0:
#     l.append(n)
# print l
#
# for i in range(len(l)):
#     print sum(l[i])


##2正确答案
lst=[]
num= map(int,raw_input().split(' '))
while(num!=[0,0]):         #题目要求输入0 0结束
    lst.append(num)
    num=map(int,raw_input().split(' '))     #这一点还不太清楚为什么要这样写
for i in range(len(lst)):
    print sum(lst[i])


##3这段是在网上找的答案，这段只是输入一个值
# list=[]
# num= int(input('shuru:'))
# while(num<>0):
#     list.append(num)
#     num= int(input('shuru:'))
# print list
