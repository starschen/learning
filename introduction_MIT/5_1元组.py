#encoding:utf8
#5_1元组

# def findDivisors(n1,n2):
#     '''假定n1,n2是正整数
#        返回一个元组，包含n1,n2的公约数'''
#     divisors=()
#     for i in range(1,min(n1,n2)+1):
#         if n1%i==0 and n2%i==0:
#             divisors=divsors+(i,)
#     return divisors
#
# divisors=findDivisors(20,120)
# print divisors
# total=0
# for d in divisors:
#     total+=d
# print total

def findExtremeDivisors(n1,n2):
    '''假定n1,n2是正整数
       返回一个元组，包含n1,n2的最小公约数和最大公纸数，最小公约数大于1'''
    divisors=()
    minVal,maxVal=None,None
    for i in range(2,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            if minVal==None or i<minVal:
                minVal=i
            if maxVal==None or i>maxVal:
                maxVal=i
    return (minVal,maxVal)

minDivisor,maxDivisor=findExtremeDivisors(100,200)
print minDivisor,maxDivisor
