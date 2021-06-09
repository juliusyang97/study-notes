import pyautogui
import pyperclip
import time

time.sleep(10) # 10秒后执行该脚本,提前打开PC端微信

while True:
    # pyautogui.typewrite("hello world") # 输入英文字符串,不能输入中文小老小老弟
    pyperclip.copy('小老弟') # 复制内容到剪贴板
    pyautogui.hotkey('ctrl', 'v') # 按下 ctrl + v 粘贴内容

    pyautogui.mouseUp()  # 模拟鼠标左键抬起
    pyautogui.moveTo(3722, 1210)  # 将鼠标移动到“发送”按钮所在的坐标
    pyautogui.mouseDown()  # 模拟鼠标左键按下
    pyautogui.mouseUp() # 模拟鼠标左键抬起
    time.sleep(1)  # 等待1秒
