#encoding:utf8
#5.3函数对象


def applyToEach(l,f):
    '''假定l是列表，f是函数
       uqf 地应用在l的每个元素上，并用返回值替换原来的元素'''
    for i in range(len(l)):
        l[i]=f(l[i])
    return l

l=[1,-2,3.33]
print 'l=',l
print 'Apply abs to each element of l.'
print applyToEach(l,abs)
print 'Apply int to each element of l.'
print applyToEach(l,int)
# print 'Apply facttorial to each element of l.'
# print applyToEach(l,4_3递归.factR)
# print 'Apply Fibonnaci to each element of l.'
# print applyToEach(l,4_3递归.fib)
