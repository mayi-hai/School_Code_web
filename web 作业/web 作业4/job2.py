import requests
import pymysql
import re
from datetime import datetime
from bs4 import BeautifulSoup


# 爬取百度新闻中特定关键词的相关新闻条目（发布时间，来源，链接），并存入mysql数据库。
url = "https://www.baidu.com/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Referer": "http://news.baidu.com/",
    "Host": "www.baidu.com",
}

# 连接数据库
con = pymysql.connect(host='localhost', user='admin', passwd='568057071', db='pythonJob', charset='utf8')
cur = con.cursor()

# 初始化数据数组
date = []
media = []
link = []

# 爬取7页数据
for i in range(0, 7):
    params = {
        'rtt': 1,
        'bsst': 1,
        'cl': 2,
        'tn': 'news',
        'word': '公路自行车',
        'rsv_dl': 'ns_pc',
        'pn': i * 10
    }
    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    for i in range(10):
        news = soup.find_all('div', {'class', 'result'})[i]

        # 每则新闻的发布媒体
        m = news.find(name="p", attrs={"class": re.compile("c-author")})
        m1 = m.text.split()[0]
        media.append(m1)

        # 每则新闻的发布时间
        t = m.text.split()[1]
        dt = datetime.strptime(t, '%Y年%m月%d日')
        d = dt.strftime('%Y-%m-%d')
        date.append(d)

        # 每则新闻的新闻链接
        href = news.h3.a['href']
        link.append(href)

# 建表，插入数据
try:
    cur.execute("create table newsData2(date char(20),media char(64),link char(128))character set utf8;")
    for i in range(0, len(date)):
        cur.execute("insert into newsData2(date,media,link) values(%s,%s,%s)",
                    (date[i], media[i], link[i]))
        con.commit()
except:
    for i in range(0, len(date)):
        cur.execute("insert into newsData2(date,media,link) values(%s,%s,%s)",
                    (date[i], media[i], link[i]))
        con.commit()
