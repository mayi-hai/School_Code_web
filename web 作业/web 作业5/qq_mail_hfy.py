# -*- coding:utf-8 -*-
# noinspection PyUnresolvedReferences
import re
import time

from selenium import webdriver

# 这里是浏览器驱动路径，也可防止系统环境变量就不用指定了
browser = webdriver.Chrome()
browser.implicitly_wait(10)

# 模拟登录qq邮箱
def qq_mail_login():
    # 打开QQ邮箱地址
    browser.get("https://mail.qq.com")

    # 切换iframe
    login_iframe = browser.find_element_by_id("login_frame")
    browser.switch_to.frame(login_iframe)
    # 点击帐号密码登录
    try:
        browser.find_element_by_id("switcher_plogin").click()
    except:
        print('请在控制台输入qq的账号密码')
    # 输入账号密码
    account = input('填入QQ')
    password = input('填入QQ密码' )
    # 添加帐号和密码
    browser.find_element_by_id("u").send_keys(account)
    browser.find_element_by_id("p").send_keys(password)

    # 点击登录
    browser.find_element_by_id("login_button").click()

def to_main_frame():
    # 点击‘收件箱’
    browser.find_element_by_id("folder_1").click()

    # 切换iframe
    main_frame = browser.find_element_by_id("mainFrame")
    browser.switch_to.frame(main_frame)

def save_mail_content():
    mail_list = browser.find_elements_by_class_name("M")
    mail_num = len(mail_list)
    title = input('输入邮件标题')
    for i in range(mail_num):
        mail_list = browser.find_elements_by_class_name("M")
        if title == mail_list[i].find_element_by_class_name('tt').text:
            mail_list[i].click()
            title = browser.find_element_by_id("subject").text
            content = browser.find_element_by_id("mailContentContainer").text
            # 将邮件内容写入文件
            fd = open(title + '.txt', mode="w", encoding="utf-8")
            fd.write(content)
            fd.close()
            # 返回邮件列表
            browser.back()
            time.sleep(2)
            browser.refresh()
            to_main_frame()

def main():
    qq_mail_login()
    to_main_frame()
    save_mail_content()

if __name__ == '__main__':
    main()
