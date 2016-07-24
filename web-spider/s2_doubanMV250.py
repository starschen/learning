#encoding:utf8
import requests
import lxml.etree
import pymysql
import numpy as np
import matplotlib.pyplot as plt
import sys
import json

reload(sys)
sys.setdefaultencoding("utf8")

douban={}

def get_page(i):
    url='https://movie.douban.com/top250?start={}&filter='.format(i)   #start={}&filter= what's the meaning of?
    html=requests.get(url).content.decode('utf-8')    #content以字节方式响应 decode
    selector=lxml.etree.HTML(html)
    # print 'selector:',selector

    #分析页面内容在 <div class='info'>
    content=selector.xpath('//div[@class="info"]/div[@class="bd"]/p/text()')
    #print 'content:',content

    for i in content[1::2]:
        #print str(i).strip().replace('\n\r','')
        if not i.strip():
            continue
        i=str(i).split('/') #电影中的不同内容分隔成几项
        i=i[-1]  #电影分类在最后，获取分隔后的最后一项是需要的电影分类
        key=i.strip().replace('\n','').split() #把电影分类的各个类分开
        #统计电影分类的个数
        for i in key:
            i = i.strip(' ')
            if i not in douban:
                douban[i]=1
            else:
                douban[i]+=1

for i in range(10):
    get_page(i*25)

for item in sorted(douban, key=douban.get, reverse=True):
    print item, douban.get(item)

# # link to mysql database
# conn=pymysql.connect(host='localhost',user='root',passwd='123321',db='mysql',charset='utf8')
# cur=conn.cursor() #获取操作游标
# # cur.execute("create table douban (id int,类别 varchar(255),数量 varchar(255))")
# cur.execute("use douban")
# #save to mysql db
# def save_mysql(douban):
#     # print douban
#     for key in douban:
#         if key!='':
#             try:
#                 sql='insert douban(类别，数量) value('+"\'"+key+"\'"+str(douban[key])+"\'"+');'
#                 cur.execute(sql)
#                 conn.commit()
#             except:
#                 print '插入失败'
#                 conn.rollback()
#     return cur
#
# print save_mysql(douban)


# # 用matplotlib进行数据可视化操作
# def pylot_show():
#     sql='select * from douban;'
#     cur.execute(sql)
#     rows=cur.fetchall() #把表中所有字段读取出来
#     count=[]   #每个分类数量
#     category=[]  #分类
#
#     for row in rows:
#         count.append(int(row[2]))
#         category.append(row[1])
#
#     y_pos=np.arrage(len(category)) #定义y轴坐标
#     plt.barh(y_pos,count,align='center',alpha=0.4) #横向条形图 alpha 图表填充不透明度
#     plt.yticks(y_pos,category) #在y轴上做分类名的标记
#
#     for count,y_pos in zip(count,y_pos):
#         #分类个数在图中显示的位置，就是数字在柱状图尾部显示的数字
#         plt.text(count,y_pos,count,horizontalalignment='center',verticallalignment='center',weight='bold')
#     plt.ylim(+28.0,-1.0)
#     plt.title('豆瓣电影250')
#     plt.ylabel('电影分类')
#     plt.subplots_adjust(bottom=0.15)
#     plt.xlabel('分类出现的次数')
#     plt.savefig('douban.png')
#     plt.show()
#
# pylot_show(cur)
