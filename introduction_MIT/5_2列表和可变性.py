#encoding:utf8
#5.2列表和可变性

# l=['I did it all',4,'love']
# for i in range(len(l)):
#     print l[i]
#
# Techs=['MIT','Caltech']
# Ivys=['Harvard','Yale','Brown']
#
# Univs=[Techs,Ivys]
# Univs1=[['MIT','Caltech'],['Harvard','Yale','Brown']]
#
# print 'Univs=',Univs
# print 'Univs1=',Univs1
# print Univs==Univs1
# print id(Univs)==id(Univs1)
# print 'Id of Univs=',id(Univs)
# print 'Id of Univs1=',id(Univs1)
#
# for e in Univs:
#     print 'Univs contains',e
#     print 'which contains'
#     for u in e:
#         print '',u

# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print 'l3=',l3
# l1.extend(l2)
# print 'l1',l1
# l1.append(l2)
# print 'l1',l1

#克隆
# def removeDups(l1,l2):
#     '''假定l1和l2是列表，
#        删除l1中出现在l2中的元素'''
#     for e1 in l1[:]:  #如果只写在l1中循环，那是有问题的，为什么加[:]就可以了呢
#         if e1 in l2:
#             l1.remove(e1)
#     print 'l1=', l1
#
# l1=[1,2,3,4]
# l2=[1,2,5,6]
# removeDups(l1,l2)

#列表生成式
l=[x**2 for x in range(1,7)]
print l

mixed=[1,2,'a',3,4.0]
print [x**2 for x in mixed if type(x)==int]
