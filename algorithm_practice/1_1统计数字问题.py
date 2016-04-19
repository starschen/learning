#encoding:utf8
##1_1统计数字问题
#
m=int(raw_input())

#习题答案中给的思路，并不是十分理解这种做法
def func(n):
    if n==1:
        return 1
    else:
        return 10*func(n-1)+10**(n-1)
print func(m)


#运用python的优势，转化为字符串再对其计数
l=map(str,range(1,m+1))
s=[]
a=[]
for i in l:
    for j in i:
        s.append(j)
for i in map(str,range(10)):
    a.append(s.count(i))
print a

#4.19本意是想用字典，把原数进行整除和求余，求得各个数的组成，但是对于一个三位数，除数没有继续循环，尝试过用while但是却死循环了
statisticnum={}.fromkeys([x for x in range(10)])#构造字典，键为0～9，值为各数字出现的次数
for key,val in statisticnum.items():
    statisticnum[key]=0
# print statisticnum
if m<10:
    for i in range(1,m+1):
        statisticnum[i]=1
else:
    for i in range(1,m+1):  #从第1页开始到第m页
        n=i%10     #求余
        # print 'n=',n
        if n in range(10):
            statisticnum[n]+=1  #余数如果是0～9，计数加1
        # print 'statisticnum=',statisticnum
        i=i/10          #除数如果0～9，计数加1，这部分如果是三位数就不继续循环了，不知道该如何表示循环
        # print 'i=',i
        if i in range(10):
            statisticnum[i]+=1

print statisticnum


#这部分是为求得几位数，但是比较麻烦，舍弃
# s={}.fromkeys(i for i in range(10))  #求得输入m的位数n
# # print 'i=',i
# for key in s.keys():
#     n=m/(10**key)
#     s[key]=n
# n=s.values().index(0)
# print n
