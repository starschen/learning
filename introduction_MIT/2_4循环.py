#encoding:utf8
#2_4循环.py
#计算整数平方的复杂方法
# x=int(raw_input('Enter an integer:'))
def sqrtint(x):
    ans=0
    itersleft=x
    while(itersleft!=0):
        ans=ans+x
        itersleft=itersleft-1
    print str(x),'*',str(x),'=',str(ans)

# sqrtint(x)
#动手练习：要求用户输入10个整数，然后输出其中最大奇数，如果没有输入奇数，输出一条信息来说明
def isodd(a):
    if a%2==1:
        return True
    else:
        return False

def maxodd(lst):
    oddlist=filter(isodd,lst)
    if len(oddlist)>0:
        print 'The max odd in this list is:',max(oddlist)
    else:
        print 'There are no odd numbers.'

n=10
l=[]
print 'Enter 10 integers:'
for i in range(n):
    x=int(raw_input())
    l.append(x)
# print l
maxodd(l)
