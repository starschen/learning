#列表操作 5.2
l.append(d)
l.count(e) #返回L中e出现的次数
l.insert(i,e)#将e插入到下标为i的位置
l.extend(l1)#将列表l1中的元素添加到l的结尾
l.remove(e)#从l中删除第一次出现的e
l.index(e)#返回l中e第一次出现的下标
l.pop(i)#删除并近回下标为i的元素
l.sort()#有副作用地排序l中的元素
l.reverse()#有副作用地番列表l

#常用文件操作 4.6
open(fn,'w')#创建一个文件用于写入内容
open(fn,'r')#打开一个已有文件用于读取内容
open(fn,'a')#找开一个已有文件用于追加内容
fh.read()#返回一个包含文件内容的字符串
fh.readline()#返回文件的下一行
fh.readlines()#返回一个列表，其中的一个元素就是文件的一行
fh.write(s)#将字符串s写到文件结尾
fh.writelines(s)#s是一个字符串序列，这条语句会将s的每个元素都写入文件
fh.close()#关闭文件

#字符串、元组和列表5.4
seq[i]
len(seq)
seq1+seq2
n*seq
seq[start:end]
e in seq
e not in seq
for e in seq
s.count(s1)#返回s中s1出现的次数
s.find(s1) #返回s1在s中第一次出现的下标，如果不在s中，返回－1
s.rfind(s1)#和find类似，但是从s的结尾开始 r reverse
s.index(s1)#和find类似，但是如果s1不在s中会抛出异常
s.rindex(s1)#和index类似，但是从s的结尾开始
s.lower()#将所有大写字母小写
s.replace(old,new)#将s中所有old子字符串替换为new
s.rstrip()#删除s结果的空白符
s.split(d)#以d为分界符，返回s的子字符列表

#常用字典操作5.5
len(d)
d.keys() #返回一个列表，包含d中的键
d.values()#返回一个列表，包含d中的值
k in d
d[k]#返回d中键为k的项
d.get(k,v)#如果k在d中，返回d[k]，否则返回v
d[k]=v#将值v与键k关联，若k已有值，则v替换原来值
del d[k]#删除键k
for k in d


#pylab
import pylab
pylab.rcParams['lines.linewidth']=4#设置线条宽度
pylab.rcParams['axex.titlesize']=20#设置标题字体大小
pylab.rcParams['axes.labelsize']=20#设置坐标轴标签的字体大小
pylab.rcParams['xtick.labelsize']=16#设置x轴数字大小
pylab.rcParams['ytick.labelsize']=16#设置y轴数字大小
pylab.rcParams['xtick.major.size']=7#设置x轴上的标记大小
pylab.rcParams['ytick.major.size']=7#设置y轴上的标记大小
pylab.rcParams['lines.markersize']=10#设置标志大小
