import os
import requests
import re
from multiprocessing.dummy import Pool

url = 'http://www.kanunu8.com/book3/6633'
html = requests.get(url).content.decode('GBK')

# 得到每个章节的url和章节名称
obj = re.findall(r'"1160(.*?)">(.*?)</a>', html, re.S)

url_list=[]
chapter = []
for i in obj:
    url_list.append(url + "/1160" + i[0])
    chapter.append(i[1])


# 提取全书每个章节内容存入代码所在目录
def query(url):
    html = requests.get(url).content.decode('GBK')
    search = re.findall(r'<p>(.*)</p>', html, re.S)
    text = search[0].replace('<br />'," ")
    title = url_list.index( url )
    path = '球状闪电 ' + chapter[title] + '.txt'
    f = open( path, 'w', encoding='utf-8' )
    f.write( text )
    f.close()

pool = Pool(4)  # 线程：4
pool.map(query, url_list)
