#encoding:utf8
##1096 A+B for input-output practice(VIII)

n=int(raw_input())
l=[]
lst=[]
for i in range(n):
    l.append(raw_input().split(' '))
    lst.append(map(int,l[i]))
for i in range(n):
    print sum(lst[i][1:]),'\n'


#另一种输出形式，输入一行输出一行
# n=int(raw_input())
# l=[]
# lst=[]
# for i in range(n):
#     l.append(raw_input().split(' '))
#     lst.append(map(int,l[i]))
#     print sum(lst[i][1:]),'\n'
