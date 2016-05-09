#encoding:utf8
#动手练习：实现一个满足下面需求的函数，要用到try－except估码块,这部分不对。5.9
# def sumDigits(s):
#     '''假设s是一个字符串
#        返回s中十进制数的和
#        例如，如果s是a2b3c，函数返回5'''
#     result=0
#     l=[]
#     for i in range(len(s)):
#         try:
#             l.append(int(s[i]))
#         except ValueError:
#
#
#     return sum(l)
#
#
#
# print sumDigits('a2b3c')


# def readIn():
#     while True:
#         val=raw_input('Enter an integer:')
#         try:
#             val=int(val)
#             a=val**2
#             print a
#             break
#         except ValueError:
#             print val,'is not an integer'
#
# def readVal(valType,requestMsg,errorMsg):
#     while True:
#         val=raw_input(requestMsg+':')
#         try:
#             val=valType(val)
#             return val
#         except ValueError:
#             print val,errorMsg
# # val=readVal(int,'Enter an integer','is not an integer')
#
#
