#encoding:utf8
import urllib
import urllib2
import logging

url='http://www.someserver.com/register.cgi'

values={'name':'WHY',
        'location':'SDU',
        'language':'Python'}

data=urllib.urlencode(values) #编码工作
req=urllib2.Request(url) #发送请求同时传data表单
logging.info('urlopen...')
response=urllib2.urlopen(req, data, timeout=3) #接受反馈的信息
logging.info('reading...')
the_page=response.read() #读取反馈内容
