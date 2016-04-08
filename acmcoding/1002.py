#encoding:utf8
#1002 A+B Problem II
#最后一个结束不应该还有空格，还没想通该怎么写

n=int(raw_input())
l=[]
for i in range(n):
    l.append(raw_input().split(' '))
    l[i]=map(int,l[i])

for i in range(n):
    print 'Case',i
    print l[i][0] ,'+',l[i][1],'=',sum(l[i])
    print ''
