#encoding:utf8
#查找最大元素

##思路：python可以直接对字母进行比较，所以考虑是逐一比较，出现最大的加（max）
##首先找到最大值 ，然后想怎么能够在最大值后面加（max），找到个函数insert(index,插入内容)，再考虑
##index(要找到的)）这个函数，是找到元素所在的位置，但是这时候出现问题了，这里的index（）只取了第一个
##最大值的位置，但题目要求将所有的最大值后面都要加(max)
##后来又考虑用替换的函数replace()


##正式答案
s=raw_input()
max_str=s[0]

for i in s:
    if i>=max_str:
        max_str=i

print s.replace(max_str,max_str+'(max)')







##v如下为寻找思路所写
#s=list(raw_input())
# s='xxxxx'
# s=list(s)
# # print s.index('c')
# # s.insert(s.index('c'),'(max)')
#
# max_str=s[0]
# #
# # for i in s:
# #     if i>=max_str:
# #         max_str=i
# for i in enumerate(s):
#     if i>=max_str:
#         max_str=i
# print max_str

#print s.index(max_str)


#
# print s.replace(max_str,max_str+'(max)')
#s.insert(s.index(max_str)+1,'(max)')

#print s
