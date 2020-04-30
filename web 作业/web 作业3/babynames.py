import sys
import re
import pymongo
import pymysql
from pymongo import MongoClient



def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  if re.search(r'[0-9]{4}', filename):
    year = re.search(r'[0-9]{4}', filename).group()
  else:
    sys.exit(1)
  f = open(filename, 'r')
  cont = f.read()
  tableData = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>')', cont) # 返回string中所有与pattern相匹配的全部字串，返回形式为数组
  f.close()

  dic = []
  for data in tableData:
    baby = {'name':data[2],'year':year,'rank':data[0]}
    dic.append(baby)
  return dic

# 建立mongodb库
#将提取数据批量插入数据库
def insert_mongo(data):
  client = MongoClient(host='localhost', port=27017)
  db = client['babyname']
  collection = db['babyData']
  collection.insert_many(data) #insert_many
  print('已将数据库存入Mongodb中')

def query_mongo(name):
  client = MongoClient(host='localhost', port=27017)
  db = client['babyname']
  collection = db['babyData']
  result = collection.find({'name':name})
  counts = collection.count_documents({'name':name}) #count_documents 计数
  if counts == 0:
    print('没有改数据')
  else:
    print('编号 名字 年号 排序')
    count = 1
    for a in result:
      print(count, a['name'], a['year'], a['rank'])
      count += 1


#建立mysql数据库
def insert_mysql(filename):
  con = pymysql.connect(host='localhost',user='root',password='123',charset='stf8')
  cur = con.cursor()
  # 开始建库
  try:
    cur.execute("create database baby character set utf8;")
    cur.execute("use baby;")
  except:
    # 使用库
    cur.execute("use baby;")

  if re.search(r'[0-9]{4}', filename):
    year = re.search(r'[0-9]{4}', filename).group()
  else:
    sys.exit(1)
  f = open(filename, 'r')
  cont = f.read()
  tableData = re.findall(r'<td>(.*)</td><td>(.*)</td><td>(.*)</td>', cont)
  f.close()

# 建表
    try:
        cur.execute("create table babyData(name char(20),year char(20),rank char(20))character set utf8;")
        for data in tableData:
            cur.execute("insert into babyData(name,year,rank) values (%s,%s,%s)", (data[2], year, data[0]))
        con.commit()
    except:
        for data in tableData:
            cur.execute("insert into babyData(name,year,rank) values (%s,%s,%s)", (data[2], year, data[0]))
        con.commit()
    # 关闭游标，数据库
    print(year, '年数据成功添加到MySQL中')
    cur.close()
    con.close()

# 排号
def query_mysql(name):
  con = pymysql.connect(host='localhost', user='root', db='baby',
                        passwd='123', charset='utf8')
  cur = con.cursor()
  print('编号 名字 年号 排名')
  sql_quert = "select * from babydata where name='%s';" % name
  num = cur.execute(sql_quert)
  if num == 0:
    print('没有改数据')
  else:
    count = 1
    for i in range(num):
      result = cur.fetchone()
      # 打印查询的结果
      str1 = str(count) + ' '
      for res in result:
        str1 = str1 + res + ' '
      print(str1)
      count += 1



def main():
  # 输入格式：python babynames.py -mo -a baby1990.html
  #python babynames.py -mo -q Alice

  args = sys.argv[1:]

  if not args:
    print('error, please input options')
    sys.exit(1)

  #print(args)
  if args[0] == '-mo':
    del args[0]       # del
    if args[0] == '-a':
      del args[0]
      for arg in args:
        baby_data = extract_names(arg) # 提取数据到baby_data
        insert_mongo(baby_data)
    elif args[0] = '-q':
      query_mongo(args[1])
  else:
    print("error :input is wrong")

  if args[0] == '-my':
    del args[0]       # del
    if args[0] == '-a':
      del args[0]
      for arg in args:
        baby_data = extract_names(arg) # 提取数据到baby_data
        insert_mysql(baby_data)
    elif args[0] = '-q':
      query_mysql(args[1])
  else:
    print("error :input is wrong")

  
if __name__ == '__main__':
  main()
