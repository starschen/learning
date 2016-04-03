#encoding:utf8
#字符串统计

#思路：先将字符串中的元素均用ASCII码表示，判断其ASCII码在48～57之间的但是数字
#这道题一开始想得很简单，想着直接用type找到list里的int不就行了，结果我忘了，当字符串以列表形式
#表示的时候数字也是str形式，所以统计数为0，后来想到可区分str和int应该就是用ASCII了

def is_num(s):
    l=list(s)
    l_asc=[]

    for i in l:
        l_asc.append(ord(i))
    #print l_asc
    lst=[]
    for j in l_asc:
        if j in range(48,59):
            lst.append(j)

    print len(lst)



is_num('asd3fghjk8496ldorj')
is_num('asdfweirfa1111awef')
