#encoding:utf8
#12.1随机程序

#掷骰子
import random

def rolldie():
    '''返回1－6之间的整数'''
    return random.choice([1,2,3,4,5,6])

def rolln(n):
    result=''
    for i in range(n):
        result=result+str(rolldie())
    print result

rolln(10)
