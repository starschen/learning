#encoding:utf8
#2011多项式求和
##这遍题目我都是没有按照题目要求的格式输入和输出，毕竟才开始学习，先能实现功能，再去规范输入输出

def pol(x):
    l=[]
    a=1
    for i in range(1,x+1):
        a=(-1.0)**(i+1)/i
        l.append(a)
    return l
#print pol(4)

def sum_pol(x):
    return round(sum(pol(x)),2)

print sum_pol(2)
print sum_pol(1)
