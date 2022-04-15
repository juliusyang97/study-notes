# Author：juliusyang

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get(
    'https:xxx')
element = wd.find_element_by_class_name('largeIcon_21')  # 这是selenium3的写法
element.click()

element = wd.find_element_by_id('username')
element.send_keys('xxx')

element = wd.find_element_by_name('password')
element.send_keys('xxx\n')

wd2 = webdriver.Chrome()
wd2.get(
    'https://xxx')
element = wd2.find_element_by_class_name('largeIcon_21')  # 这是selenium3的写法
element.click()

element = wd2.find_element_by_id('username')
element.send_keys('xxx')

element = wd2.find_element_by_name('password')
element.send_keys('xxx\n')

# 浏览器页面刷新
for i in range(3):
    wd.refresh()
    wd2.refresh()
    time.sleep(2)

wd.quit()
wd2.quit()
