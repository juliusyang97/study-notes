# Author：juliusyang

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

wd = webdriver.Chrome()
wd.implicitly_wait(20)

wd.get(
    'https:www.xxx.com')  # 这是selenium3的写法
element.click()
element = wd.find_element_by_id('username')
element.send_keys('xxx')
element = wd.find_element_by_name('password')
element.send_keys('xxx\n') # 输入密码之后回车
time.sleep(10)

num = 10000
for i in range(num):
    if num / 100 == 0:
        wd.refresh()
    try:
        element = wd.find_element_by_id('startbtn')
        element.click()
    except NoSuchElementException:
        continue
    try:
        element = wd.find_element_by_id('fwin_dialog_submit')
        element.click()
    except NoSuchElementException:
        continue
    try:
        element = wd.find_element_by_id('fwin_dialog_submit')
        element.click()
    except NoSuchElementException:
        continue

wd.quit()
