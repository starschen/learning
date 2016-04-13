#encoding:utf8
#6.2调试

#一段错误的代码
def isPal(x):
    '''假定x是列表
       如果列表是回文的返回True，否则返回False'''
    temp=x[:]
    # temp.reverse        #错误，没有加括号
    temp.reverse()        #修改后
    if temp == x:
        return True
    else:
        return False

def silly(n):
    '''假定n是正整数
       接受用户的n个输入
       如果所有输入组成了一个回文列表，返回‘Yes’
       否则返回‘No’'''
    result=[]                   #修改后
    for i in range(n):
        # result=[]            ＃在循环里相当于每次循环都会清空
        elem=raw_input('Enter element:')
        result.append(elem)
    print result
    if isPal(result):
        print 'Yes'
    else:
        print 'No'

silly(2)
