#encoding:utf8
#数列有序

#这道python做就很简单了，因为python有自带的排序函数，还可将列表相加，这道题的思路就是两个列表相加，然后排序。
#这道题对于输入 0 0就退出，什么都不做不太会表示
#还有这道题的输出还有些疑问，后续再考虑

l1=raw_input().split(' ')

# if l1==['0','0']:
#     break             #break 会报错

l2=raw_input().split(' ')

s=l1+l2
s=sorted(list(set(s)))
l=[]

for i in s:
    l.append(int(i))

for j in l:
    print j
