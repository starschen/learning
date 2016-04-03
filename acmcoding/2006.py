#encoding:utf8
##2006求奇数的乘积

def odd(x):
    if x%2!=0:
        return True
    else:
        return False

def odd_mult(L):
    lst=filter(odd,L)
    if len(lst)==0:    #判断列表是否有奇数
        return 'There is no odd in the list.'
    else:
        lst1=set(lst)  #去重
        num=1
        for i in lst1:
            num=num*i
        return num

print odd_mult([3,1,2,3])
print odd_mult([4,2,3,4,5])
print odd_mult([2,4,4,6,8])
