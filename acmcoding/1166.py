#encoding:utf8
##敌兵布阵

##问题1：未加入人数判断条件
import math
command=[]
t=len(command)      #t tiao ming ling
T=int(raw_input())    #共T组数据
for i in range(0,T):   #
    N=int(raw_input())        #每组共有N个工兵营地
    a=map(int,raw_input().split(' '))  #每个工兵营地的人数 例 1 2 3 4  #这里人数要求1<=ai<=50
    # print 'Case',T,':'
    while t<=40000 :
        command=raw_input().split(' ')
        if command=='End':
            break
        else:
            i=int(command[1])-1       #第i个营地,此处用-1是因为列表是从0开始计，i不超过30
            j=int(command[2])        #j不超过30
            if command[0]=='Query':
                print sum(a[i:j])
            elif command[0]=='Add':
                a[i]=a[i]+j        #第i个营地增加j个人
            elif command[0]=='Sub':
                a[i]=a[i]-j
            else:
                break
