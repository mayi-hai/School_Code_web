# web数据挖掘与电子商务周学习计划与作业要求(第4周，3月16日-3月22日)



## 学习目标
1. 学习Python数据库编程
2. 学习Mysql与MongoDB开发

 
## 学习计划
1. 【MogoDB】学习[web数据挖掘与电子商务](http://mooc1.chaoxing.com/course/208399347.html "web数据挖掘与电子商务")的预备知识章节内容中的3.3；
2. 【MySql】学习：
(1) [下载页面](https://dev.mysql.com/downloads/mysql/5.7.html "下载页面") **根据自己的系统选择32bit或者64bit的压缩包**
(2) [安装教程](https://dev.mysql.com/doc/refman/5.7/en/windows-install-archive.html "安装教程")
(3) [安装管理器Navicat](https://my.oschina.net/ZL520/blog/3070953 "安装管理器Navicat")
(4) [Python MySql](https://www.w3schools.com/python/python_mysql_getstarted.asp "Python MySql")
3. 一个整合在线编译器的在线学Python网站：[learnpython](https://www.learnpython.org/ "learnpython")

## 作业要求
第4周作业要求：
1. 基于作业2的代码，利用所学的Python MogoDB编程和MySql编程知识，将提取的baby names信息分别存入MogoDB和MySql数据库，存储内容格式为：

| name | year | rank |
| ---- | ---- | ---- |
| Andy | 1990 | 2 |

2. 程序运行要求，假设python程序文件名为"baby.py"，在命令行下输入如下命令后，需实现的功能：
```
c:\>python baby.py -mo -s xxx.html //xxx.html文件中的name相关信息存入MogoDB数据库
```
```
c:\>python baby.py -my -s xxx.html //xxx.html文件中的name相关信息存入MySql数据库
```
```
c:\>python baby.py -mo -q xxx //MongoDB数据库中name为xxx的名字信息打印出来
```
```
c:\>python baby.py -my -q xxx //Mysql数据库中name为xxx的名字信息打印出来
```
上述两条命令的打印格式为：
> 编号 名字 年号 排名
>
> 1 xxx 1990 12
>
> 2 xxx 1991 45
>
> ...


作业提交时请打包，打包文件标题格式为：作业3:xxx，xxx为自己的姓名，提交截止时间2020年3月29日(星期日)20点，请大家统一将打包文件在截至时间之前发给学习委员 ***陈慧*** 同学。***陈慧*** 同学，不管是否收齐作业，请务必于2020年3月29日20点10分之前（以邮件时间为准）将收到的作业打包以附件形式发到我的QQ邮箱：93315045@qq.com，邮件标题为：“web数据挖掘与电子商务，作业2”
**请各位认真学习在线课程，仔细阅读作业要求，并完成相关作业。作业成绩将根据上述内容与格式要求进行评定。**
