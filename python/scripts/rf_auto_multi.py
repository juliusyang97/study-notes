# Author：juliusyang

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

wd = webdriver.Chrome()
wd.implicitly_wait(0.5)
wd.get('https://xxx')
element = wd.find_element_by_class_name('largeIcon_21')  # 这是selenium3的写法
element.click()
element = wd.find_element_by_id('username')
element.send_keys('username')
element = wd.find_element_by_name('password')
element.send_keys('password\n')
time.sleep(8)

num = 1000
for i in range(num):
    js = "window.open('{}','_blank')"
    if i == 0:
        wd.execute_script(js.format("https:/xxx"))
        time.sleep(1)
        wd.execute_script(js.format('https://xxx'))
        time.sleep(1)
        wd.execute_script(js.format('https://xxx'))
        time.sleep(1)

    wd.switch_to.window(wd.window_handles[0])
    # time.sleep(2)
    if i == 0:
        try:
            element = wd.find_element_by_id('startbtn').click()
        except NoSuchElementException:
            pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass

    time.sleep(1)
    wd.switch_to.window(wd.window_handles[1])
    if i == 0:
        try:
            element = wd.find_element_by_id('startbtn')
            element.click()
        except NoSuchElementException:
            pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass

    time.sleep(1)
    wd.switch_to.window(wd.window_handles[2])
    if i == 0:
        try:
            element = wd.find_element_by_id('startbtn')
            element.click()
        except NoSuchElementException:
            pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass

    time.sleep(1)
    wd.switch_to.window(wd.window_handles[3])
    if i == 0:
        try:
            element = wd.find_element_by_id('startbtn')
            element.click()
        except NoSuchElementException:
            pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    try:
        element = wd.find_element_by_id('fwin_dialog_submit').send_keys(Keys.ENTER)
        # element.click()
    except NoSuchElementException:
        pass
    time.sleep(1)
wd.quit()
