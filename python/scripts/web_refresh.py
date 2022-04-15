# -*- coding: utf-8 -*-

import sys


from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class WebView(QWebEngineView):
    def __init__(self):
        super(WebView, self).__init__()
        #url = 'https://blog.51cto.com/u_15169037/2711577'  # 自定义刷新的网页
        url = 'https://rohm.eefocus.com/module/forum/forum.php'
        self.load(QUrl(url))
        self.showMinimized()  #窗口最小化
        self.show()
        self.thread = Worker()  # 创建线程实例
        self.thread.sinOut.connect(self.reloadWeb)  # 信号绑定槽函数
        self.thread.start()  # 开启线程


    def reloadWeb(self):
        self.reload() #刷新网页


class Worker(QThread):
    sinOut = pyqtSignal()  # 创建新的信号，并且有参数
    num = 0
    def __init__(self, parent=None):  # 构造方法 创建号对象之后，会自动调用
        super(Worker, self).__init__(parent)


    def __del__(self):  # 析构函数 再对象被删除 和 回收的时候调用
        self.wait()

    def run(self):
        for i in range(1000):
            # 发出信号
            self.sinOut.emit()  # 给信号传参字符串，并发送
            # 线程休眠66秒
            self.sleep(60)
            Worker.num = Worker.num + 1
            print (str(Worker.num) + " 次刷新")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    web = WebView()
    print('### exec succeed !')
    sys.exit(app.exec_())

