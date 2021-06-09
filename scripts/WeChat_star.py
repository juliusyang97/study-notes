import time

import uiautomator2 as ui2

d = ui2.connect('http://172.18.105.47:7912')
d.app_start("com.tencent.mm", stop="True")
fs = d(resourceId="com.tencent.mm:id/sh")[2]
time.sleep(1)
fs.click()
pyq = d(resourceId="android:id/title")
if len(pyq):
    time.sleep(1)
    pyq[0].click()
stop_flag = False
while not stop_flag:
    eud = d(resourceId="com.tencent.mm:id/eud")
    for i in eud:
        # likeandcommand = d(resourceId="com.tencent.mm:id/eop",description="评论")
        likeandcommand = i.child(resourceId="com.tencent.mm:id/eop")

        if len(likeandcommand):
            for item in likeandcommand:
                item.click()
                d.toast.show("准备点赞")
                like = d(resourceId="com.tencent.mm:id/eoc", text="赞")
                if len(like):
                    like[0].click()
                time.sleep(1)
    d.swipe(0.2, 0.9, 0.2, 0.55)
    time.sleep(1)