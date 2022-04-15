from time import sleep

from selenium import webdriver

driver= webdriver.Chrome() #  需要 下载 对应浏览器 驱动到 python 安装目录
# 浏览器驱动对应网站：https://registry.npmmirror.com/binary.html?path=chromedriver/

driver.get("https://rohm.eefocus.com/module/forum/forum.php") # 刷新网址

for i in range(100000): # 刷新次数
    driver.refresh()  # 刷新网页
    sleep(60) # 五秒一次
