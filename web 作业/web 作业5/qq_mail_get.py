from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# noinspection PyUnresolvedReferences
from config import *
# noinspection PyUnresolvedReferences
import time
import re
import os

# 这里是浏览器驱动路径，也可防止系统环境变量就不用指定了
browser = webdriver.Chrome(executable_path="chromedriver.exe")
wait = WebDriverWait(browser, 10)   # 设置下隐式等待时间10s
bookname='QQmail'
if not os.path.exists('./' + bookname):
    os.makedirs('./' + bookname)

def mail_qq_login():
    try:
        browser.get("https://mail.qq.com/")
        browser.switch_to.frame("login_frame")
        login_bt = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#switcher_plogin'))
        )
        login_bt.click()    # 账号密码登录
        qq_nb = wait.until(
            EC.presence_of_element_located((By.ID,"u"))
        )
        qq_pw = wait.until(
            EC.presence_of_element_located((By.ID,"p"))
        )
        login_bt = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"#login_button"))
        )
        #qq_nb.send_keys('account')  # 填入QQ账号
        #qq_pw.send_keys('passwod')  # 填入QQ密码
        qq_nb.send_keys('3058105385')  # 填入QQ账号
        qq_pw.send_keys('DCYqwe123456789')  # 填入QQ密码
        login_bt.click()
    except TimeoutException:
        print("超时错误，重新登录...")
        mail_qq_login()


pattern = re.compile("^测试.*")    # 这里将“测试”替换为要提取的邮件标题的一部分 如标题为ABCDE 可替换为AB/ABC


def print_one_unread_mail(index):
    try:
        mail_list = browser.find_elements_by_css_selector('.tf.no')
        if re.match(pattern, mail_list[index].find_element_by_class_name('tt').text):
            title=mail_list[index].find_element_by_class_name('tt').text
            mail_list[index].click()
            text = browser.find_element_by_id('mailContentContainer').text
            with open('./%s/%s.txt' % (bookname, title), 'w', encoding='gbk')as f:
                f.write(text)
            browser.back()
            browser.refresh()
            recv_option = wait.until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "收件箱"))
            )
            recv_option.click()
            main_frame = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#mainFrame"))
            )
            browser.switch_to.frame(main_frame)
        else:
            return
    except TimeoutException:
        print_one_unread_mail(index)



def main():
    mail_qq_login()
    recv_option = wait.until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "收件箱"))
    )
    recv_option.click()

    main_frame = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#mainFrame"))
    )
    browser.switch_to.frame(main_frame)
    mail_list = browser.find_elements_by_class_name("M")
    mail_num = len(mail_list)

    mail_list = browser.find_elements_by_css_selector('.tf.no')
    for i in range(len(mail_list)):
        print_one_unread_mail(i)


if __name__ == '__main__':
    main()
