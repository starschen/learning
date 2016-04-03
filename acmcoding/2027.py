#encoding:utf8
##统计元音

##目前存在的问题：
##1\题意要求最后一组计数出来不输出空格，以下代码输出还是有空格。3.23
##2\按测试出来结果有一个字母o计数不对，第二组测试实例o应为0，以下代码输出为1  3.23

n=int(raw_input())            #输入测试实例个数
l=[]
for i in range(0,n):       #分行输入测试实例
    l.append(raw_input())

#测试给定输入
# n=2
# l=['aeiou','my name is ignatius']

vowel=['a','e','i','o','u']
#思路1：对列表中所有字母计数，输出元音字母数字
str_num={}              #定义对所有元素计数的字典
for i in l:             #在l中每一个字符串i循环
    for j in i:          #在字符串i中对每一个元素j循环
        str_num[j]=i.count(j)       #对元素ｊ计数，并加入str_num中
    for k in vowel:
        vowel_num=str_num[k]       #在str_num中找到vowel中的元音字母的值，赋给vowel_num

        print k,':',vowel_num
    print '\n'


#统计元音   还没做完 做不出来了   以下写的时间为3.21
##思路1：创建字典，字典键值为元音，如果输入元素的值等于字典的key,则计数＋1，最后输出字典，对于输入
##的list中的元素如何一一与字典只的键值做比较，在循环时发生字典键值不能迭代的问题
# def count_vowel(l):
#     vowel=['a','e','i','o','u']
#     vowel_num={}.fromkeys(vowel)
#     count=0
#     for i in l:
#         if i in vowel_num:
#             count+=1
#         vowel_num[i]=count
#
#     return vowel_num


# l1=list('aeiou')
# l2=list('my name is ignatius')
# s=[l1,l2]

##思路2:将输入list所有字母计数，输出其中元音字母的重复次数
##思路21 库函数计数
# from collections import Counter
# for i in s:
#     print Counter(i)

##思路22 字典计数
# def count_num(l):
#     countnum={}
#     for i in l:
#         if l.count(i)>=1:
#             countnum[i]=l.count(i)
#     return countnum
#
# count_vowel=[]
# vowel=['a','e','i','o','u']
# for l in s:
#     for i in vowel:
#         count_vowel.append(count_num(l).get(i))
#     print count_vowel



##输入
# n=int(raw_input())
# l=[]
# for i in range(0,n):
#     s=list(raw_input())
#     l.extend([s])




#先不考虑输入格式
# n=2
# l=['a','e','i','o','u']
# l1=list('aeiou')
# l2=list('my name is ignatius')
# s=[l1,l2]
# print s
# for i in range(0,len(s)):
#     for j in range
