#encoding:utf8
##2005第几天

#判断是否是闰年
def is_leap(x):
    if (x%400==0) or ((x%4==0) and (x%100!=0)):
        return True
    return False

def days(date):
    l_str=date.split('/')
    l_num=[int(i) for i in l_str]  #将输入字符串变为整型
    #print l_num
    month_day={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if is_leap(l_num[0]):
        month_day[2]=29
    #print month_day

    if l_num[1]==1:
        return l_num[2]
    else:
        sum=0              #初始化不要放在循环里，要不结果会出现错误
        for i in range(1,l_num[1]):
            sum=sum+month_day[i]
        #print sum
        return sum+l_num[2]

print days('1985/1/20')
print days('2006/3/12')
print days('2000/3/12')
print days('2016/3/12')
print days('2100/3/12')

##以下代码是写代码时验证split是否能正确工作
# date='1985/1/20'
# l_str=date.split('/')
# l_num=[int(i) for i in l_str]
# print l_num
