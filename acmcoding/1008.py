#encoding:utf8
##1008 Elevator

up=6
down=4
stop=5
s=[]

l=map(int,raw_input().split(' '))
while(l!=[0]):
    s.append(l)
    l=map(int,raw_input().split(' '))
    for i in range(len(l)):
        for j in range(1,len(l[i])):
            if (j<len(i)-1) and l[i][j]<l[i][j+1]:
                sum=stop*(len(l[i])-1)+
