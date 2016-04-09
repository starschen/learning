#encoding:utf8
#4.6文件

# nameHandle=open('kids','w') #创建文件名为kids的文件，使用‘w’写入模式打开文件
# for i in range(2):
#     name=raw_input('Enter name: ')
#     nameHandle.write(name + '\n')
# nameHandle.close()

# nameHandle=open('kids','r')
# for line in nameHandle:
#     print line
# nameHandle.close()

##会把之前的覆盖
# nameHandle=open('kids','w')
# nameHandle.write('Michael\n')
# nameHandle.write('Mark\n')
# nameHandle.close()
# nameHandle=open('kids','r')
# for line in nameHandle:
#     print line[:-1]
# nameHandle.close()

##不覆盖，追加模式
nameHandle=open('kids','a')
nameHandle.write('David\n')
nameHandle.write('Andrea\n')
nameHandle.close()
nameHandle=open('kids','r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()

#常用文件操作
open(fn,'w')#创建一个文件用于写入内容
open(fn,'r')#打开一个已有文件用于读取内容
open(fn,'a')#找开一个已有文件用于追加内容
fh.read()#返回一个包含文件内容的字符串
fh.readline()#返回文件的下一行
fh.readlines()#返回一个列表，其中的一个元素就是文件的一行
fh.write(s)#将字符串s写到文件结尾
fh.writelines(s)#s是一个字符串序列，这条语句会将s的每个元素都写入文件
fh.close()#关闭文件
