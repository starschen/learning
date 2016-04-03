#encoding:utf8
##1048 The Hardest Problem Ever

#这道题不知道为什么输入ENDOFINPUT就是结束不了，结果返回的也不对要
flag=raw_input()
lst=[]
while(flag!='ENDOFINPUT'):
    flag=raw_input()
    print flag
    while(flag!='END'):
        if flag=='START':
            l=raw_input().split(' ')
            print l
            for i in l:
                for j in i:
                    if j>='A' and j<='E':
                        m=ord(j)+21
                    else:
                        m=ord(j)-5
                    print m
                lst.append(chr(m))
    print lst
















#
# l=[]
# lst=[]
# if (n=='START' and n!='END'):
#     #while(n!='END'):
#     l=raw_input().split(' ')
#     for i in l:
#         for j in i:
#             m=ord(j)-5
#             lst.append(chr(m))
# elif (n=='END'):
#     print lst
# elif (n=='ENDOFINPUT'):
#     print
