#encoding:utf8

##2004成绩转换

##1
#我是想通过字典，输入值与字典值做比较，输入值在哪个值里面，相应的输出其对应的键值， 但是还没能理解透字典的用法，不成功，后续再弄3.15
# def scorechange(x):
#     dic={'A':range(90,101),'B':range(80,90),'C':range(70,80),'D':range(60,70),'E':range(0,60)}
#     for i in dic.keys():
#         if x in dic[i]:
#             return i
#     return 'Score is error!' #原来这句是在if语句下的,结果错误,发现if语句是从字典第一个开始遍历,如果第一个不存在就直接返回error,而我们所需要的是
#     #要在整个字典遍历完成后如果没有再返回error 3.16
#
#
# print scorechange(56)
# print scorechange(67)
# print scorechange(100)
# print scorechange(123)

#以下是为了验证上部分代码哪里出了问题
# x=80
# dic={'A':range(90,101),'B':range(80,90),'C':range(70,80),'D':range(60,70),'E':range(0,60)}
# for i in dic.keys():
#     # print i
#     # print dic[i]
#     if x in dic[i]:
#         print i




# #2
# def scorechange(x):
#     if x in range(90,101):
#         return 'A'
#     elif x in range(80,90):
#         return 'B'
#     elif x in range(70,80):
#         return 'C'
#     elif x in range(60,70):
#         return 'D'
#     elif x in range(0,60):
#         return 'E'
#     else:
#         return 'Score is error'
#
# print scorechange(56)
# print scorechange(67)
# print scorechange(100)
# print scorechange(123)

##3  
def scorechange(x):
    #dic={'A':9,'B':8,'C':7,'D':6,'E':range(0,6)}
    dic={10:'A',9:'A',8:'B',7:'C',6:'D',5:'E',4:'E',3:'E',2:'E',1:'E',0:'E'}
    return dic.get(x/10,'Score is error')

# print scorechange(56)
# print scorechange(67)
# print scorechange(100)
# print scorechange(123)

#测试用例
for x in range(-100,100):
    print scorechange(x)
