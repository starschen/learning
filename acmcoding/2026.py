#encoding:utf8
#首字母变大写

l=raw_input()
l=l.split(' ')

#l=['i','like','acm']
s=[]
for i in l:
    s.append(i.capitalize())  #str.capitalize()要注意是对str首字母大写

s=' '.join(s)    #将s中的元素以空格合并
print s
