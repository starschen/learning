#encoding:utf8
#求平均成绩

##思路：
##正式答案
import numpy as np
l1=raw_input('请输入学生数量和课程数量: ').split(' ')
l1=map(int,l1)
l2=[]
for i in range(0,l1[0]):
    l2.append(raw_input().split(' '))
l2=np.array(l2,dtype=int)

student_avg=np.average(l2,axis=1)
course_avg=np.average(l2,axis=0)
print l2
print course_avg
comp=l2>=course_avg
＃print comp
print len(filter(lambda x:x.all(),comp))


##寻找思路所写
# l1=raw_input('请输入学生数量和课程数量: ').split(' ')
# l1=map(int,l1)
# l2=[]
# for i in range(0,l1[0]):
#     l2.append(raw_input().split(' '))
# #l2=np.array(l2,dtype=int)

#print l2

# student_avg=np.sum(l2,axis=1,dtype=float)/l1[0]
# #print student_avg
# course_avg=np.sum(l2,axis=0,dtype=float)/l1[1]
# #print course_avg
# #我想将学生成绩与课程成绩做差，然后找到矩阵中行大于0的，再计数，但是比较麻烦，可以直接比较
# l3=l2-course_avg
# print l3




# l1=[2,2]
# l2=np.array([[2,3],[4,5]])
# student_avg=np.average(l2,axis=1)
# course_avg=np.average(l2,axis=0)
# print l2
# print course_avg
# comp=l2>=course_avg
# print comp
# print len(filter(lambda x:x.all(),comp))

##之前就是不知道该怎么将矩阵的行相加或列相加，才找的numpy这个库，但是觉得这个循环还是应该要知道，
##又重新考虑如何表示
l1=[2,2]
l2=np.array([[2,3],[4,5]])
l3=[] #行相加
sum=l2[0][0]
for i in range(0,l1[0]):
    sum=0       #每次sum求完之后要归零，要不会一直加
    for j in range(0,l1[1]):
        sum=sum+l2[i][j]
    l3.append(sum)
print l3
l4=[]  #列相加
for i in range(0,l1[1]):
    sum=0
    for j in range(0,l1[0]):
        sum=sum+l2[j][i]   #列相加需要注意i,j的位置
    l4.append(sum)
print l4
