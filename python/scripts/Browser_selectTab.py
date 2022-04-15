# Python实现模拟按键切换浏览器标签
# author：juliusyang

import time
import win32api
import win32con

'''
  字母和数字键     数字小键盘的键       功能键         其它键 
   键   键码       键   键码          键   键码       键      键码 
   A   65          0   96            F1   112       Backspace    8 
   B   66          1   97            F2   113       Tab       9 
   C   67          2   98            F3   114       Clear      12 
   D   68          3   99            F4   115       Enter      13 
   E   69          4   100           F5   116       Shift      16 
   F   70          5   101           F6   117       Control     17 
   G   71          6   102           F7   118       Alt       18 
   H   72          7   103           F8   119       Caps Lock    20 
   I   73          8   104           F9   120       Esc       27 
   J   74          9   105           F10  121       Spacebar    32 
   K   75          *   106           F11  122       Page Up     33 
   L   76          +   107           F12  123       Page Down    34 
   M   77        Enter 108                          End       35 
   N   78          -   109                          Home      36 
   O   79          .   110                          Left Arrow   37 
   P   80          /   111                          Up Arrow    38 
   Q   81                                           Right Arrow   39 
   R   82                                           Down Arrow    40 
   S   83                                           Insert      45 
   T   84                                           Delete      46 
   U   85                                           Help       47 
   V   86                                           Num Lock     144   
   W   87          
   X   88      
   Y   89      
   Z   90      
   0   48      
   1   49      
   2   50       
   3   51       
   4   52       
   5   53       
   6   54       
   7   55       
   8   56       
   9   57
'''

for i in range(1000):
    time.sleep(10)
    # ctrl + 1
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(49, 0, 0, 0)  # 1键位码是49
    win32api.keybd_event(49, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(10)
    # ctrl + 2
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(50, 0, 0, 0)  # 2键位码是50
    win32api.keybd_event(50, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(10)
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(51, 0, 0, 0)  # 3键位码是51
    win32api.keybd_event(51, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(10)
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(52, 0, 0, 0)  # 4键位码是52
    win32api.keybd_event(52, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(10)
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(53, 0, 0, 0)  # 5键位码是53
    win32api.keybd_event(53, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(10)
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(54, 0, 0, 0)  # 6键位码是54
    win32api.keybd_event(54, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

