# Python3 & OpenCV 视频转字符动画

## 简介

#### 1.1 知识点

- OpenCV 编译
- 使用 OpenCV 处理图片、视频
- 图片转字符画原理
- 守护线程
- 光标定位转义编码

#### 1.2 实验环境

- python 3.5
- opencv-python-3.4.1
- pyprind-2.11.2



## 实现

首先，我们来安装opencv-python:

```bash
$ sudo pip3 install opencv-python
```



### 程序原理

大家应该都明白视频其实可以看作一系列图片组成的，因此视频转字符动画最基本的便是图片转字符画，这一部分内容也在 [Python 图片转字符画](https://www.shiyanlou.com/courses/370) 课程中有讲过。

在这里简单的说一下图片转字符画的原理：首先将图片转为灰度图，每个像素都只有亮度信息（用 0~255 表示）。然后我们构建一个有限字符集合，其中的每一个字符都与一段亮度范围对应，我们便可以根据此对应关系以及像素的亮度信息把每一个像素用对应的字符表示，这样字符画就形成了。

字符动画要能播放才有意义。最最简单粗暴的，用文本编辑器打开字符动画文本文件，然后狂按 *PageDown* 键就能播放。然而这真的太简单太粗暴了，一点都不优雅。

我们还是在终端里面播放字符动画，只需要一帧一帧输出就能达到动画的效果了，然而这却有一个很大的弊端：播放时，你会发现终端右边的滚动条会越来越小（如果有的话）；播放完毕后，在终端中往上翻页，全是之前输出的字符画，播放前的命令历史全部被挤占掉了。在本实验后面提供了这个问题的解决办法。



### 程序实现

在 `/home/shiyanlou/Code` 目录下新建 `CLIPlayVideo.py` 文件，并向其中输入如下代码：

为了避免忘记，先导入会使用到的包：

```python
import sys
import os
import time
import threading
import termios
import tty
import cv2
import pyprind
```

最后一个 *pyprind* 模块提供显示用的进度条。因为从视频转为字符动画是一个耗时的过程，我们需要一个进度条来查看任务进度以及大致剩余时间，能更直观的了解程序状态。这样安装它：

```sh
$ sudo pip3 install pyprind
```

本实验将编写的程序除了能将视频文件转为字符动画并播放外，还顺便把图片文件转字符画的功能也添加上了，因此我们的程序设计有三个类：`CharFrame`、`I2Char`、`V2Char`，后两个类继承自第一个类。

*CharFrame* 类：

```python
class CharFrame:

    ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # 像素映射到字符
    def pixelToChar(self, luminance):
        return self.ascii_char[int(luminance/256*len(self.ascii_char))]

    # 将普通帧转为 ASCII 字符帧
    def convert(self, img, limitSize=-1, fill=False, wrap=False):
        if limitSize != -1 and (img.shape[0] > limitSize[1] or img.shape[1] > limitSize[0]):
            img = cv2.resize(img, limitSize, interpolation=cv2.INTER_AREA)
        ascii_frame = ''
        blank = ''
        if fill:
            blank += ' '*(limitSize[0]-img.shape[1])
        if wrap:
            blank += '\n'
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                ascii_frame += self.pixelToChar(img[i,j])
            ascii_frame += blank
        return ascii_frame
```

属性 `ascii_char` 可以根据你要转换的视频进行针对性调整。

`pixelToChar()` 方法只有一个参数，其接收像素的亮度信息。需要注意的是，方法的 `return` 语句中的表达式使用了一个数值 `256`，虽然像素的亮度范围是 `0~255`，但若是把 `256` 更改为 `255`，那么这个表达式将有可能引发 `IndexError` 异常。

`convert()` 方法有一个位置参数三个可选参数，参数 `img` 接收一个对象，这个对象类型是 `numpy.ndarray`，也就是 OpenCV 打开图片返回的对象，同样，之后用 OpenCV 得到的视频的帧也是这个对象。`limitSize` 参数接受一个元组，表示图片的限宽限高。`fill` 表示是否用空格填充图片宽度至限宽，`wrap` 表示是否在行末添加换行符。

`img.shape` 返回一个元组，含有图片的行数（高），列数（宽），以及颜色通道数。如果图片为灰度图则不包含颜色通道数。

`cv2.resize()` 函数用于缩放图片大小，第一个参数为 `numpy.ndarray` 对象，第二个是将缩放的宽高，`interpolation` 参数为插值方法。有几个插值方法可用，引用 OpenCV 官网的说明：

> Preferable interpolation methods are **cv2.INTER_AREA** for shrinking and **cv2.INTER_CUBIC** (slow) & **cv2.INTER_LINEAR** for zooming. By default, interpolation method used is **cv2.INTER_LINEAR** for all resizing purposes.

`img[i,j]` 返回图片第 i 行第 j 列像素 BGR 值构成的列表，灰度图片则为直接返回对应像素的亮度值。

下面是继承自 `CharFrame` 的 `I2Char` 类：

```python
class I2Char(CharFrame):

    result = None

    def __init__(self, path, limitSize=-1, fill=False, wrap=False):
        self.genCharImage(path, limitSize, fill, wrap)

    def genCharImage(self, path, limitSize=-1, fill=False, wrap=False):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return
        self.result = self.convert(img, limitSize, fill, wrap)

    def show(self, stream = 2):
        if self.result is None:
            return
        if stream == 1 and os.isatty(sys.stdout.fileno()):
            self.streamOut = sys.stdout.write
            self.streamFlush = sys.stdout.flush
        elif stream == 2 and os.isatty(sys.stderr.fileno()):
            self.streamOut = sys.stderr.write
            self.streamFlush = sys.stderr.flush
        elif hasattr(stream, 'write'):
            self.streamOut = stream.write
            self.streamFlush = stream.flush
        self.streamOut(self.result)
        self.streamFlush()
        self.streamOut('\n')
```

`cv2.imread()` 读取一个图片，返回一个 `numpy.ndarray` 对象。第一个参数为要打开的图片路径，第二个参数指定图片的打开方式，可以具有下面三个值：

- `cv2.IMREAD_COLOR` : 加载彩色图片，忽略透明通道。
- `cv2.IMREAD_GRAYSCALE` : 以灰度模式加载 图片。
- `cv2.IMREAD_UNCHANGED` : 加载包含透明通道的图片。

`show()` 方法接受一个参数，表示使用哪种输出流。`1` 代表输出流使用标准输出 `sys.stdout`，`2` 代表输出流使用标准错误输出 `sys.stderr`。其中 `sys.stdout.fileno()` 和 `sys.stderr.fileno()` 分别返回标准输出和标准错误输出的[文件描述符](https://zh.wikipedia.org/wiki/文件描述符)。`os.isatty(fd)` 返回一个布尔值，当文件描述符 fd 是打开并连接到 tty 设备时返回真。

然后便是我们的重点了，继承自 `CharFrame` 类的 `V2Char` 类。

先设想一下我们的类，类的其中一个属性为 `charVideo` ，这是一个列表，用来存放字符动画全部数据。

然后是两个主要方法：一个是从视频文件转为字符动画的方法 `genCharVideo()`，一个是播放字符动画的方法 `play()`。

另外由于从视频转到字符动画是一个耗时耗力的过程，所以我们可以把 `charVideo` 中的字符动画数据导出来，方便下次读取播放，这就意味着要有导出和读取方法，即 `export()` 方法和 `load()` 方法。

类还要有一个初始化方法，参数为要读取的文件路径，文件若是导出的 txt，则调用 `load()` 方法把数据加载到属性 `charVideo` 里。否则视为视频文件，调用 `genCharVideo()` 方法将视频转化为字符动画存放到属性 `charVideo` 里：

```python
def __init__(self, path):
    if path.endswith('txt'):
        self.load(path)
    else:
        self.genCharVideo(path)
```

接下来是 `genCharVideo()` 方法：

```python
def genCharVideo(self, filepath):
    self.charVideo = []
    cap = cv2.VideoCapture(filepath)
    self.timeInterval = round(1/cap.get(5), 3)
    nf = int(cap.get(7))
    print('Generate char video, please wait...')
    for i in pyprind.prog_bar(range(nf)):
        rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
        frame = self.convert(rawFrame, os.get_terminal_size(), fill=True)
        self.charVideo.append(frame)
    cap.release()
```

用 `cv2.VideoCapture()` 方法读取视频文件，生成的对象我们赋值给 `cap`。

通过 `cap.get()` 方法我们可以获得视频的属性信息，比如 `cap.get(3)` 和 `cap.get(4)` 分别返回视频的宽高信息，`cap.get(5)` 则返回视频的帧率，`cap.get(7)` 返回视频的总帧数。

`timeInterval` 存放播放时间间隔，用来让之后播放字符动画的帧率与原视频相同。

`pyprind.prog_bar()` 是一个生成器，使用这个生成器进行迭代会自然在终端中输出进度条。

`cap.read()` 读取视频的下一帧，其返回一个两元素的元组，第一个元素为 `bool` 值，指示帧是否被正确读取，第二个元素为 `numpy.ndarray` ，其存放的便是帧的数据。

`cv2.cvtColor()` 用来转换图像的颜色空间，第一个参数为图像对象，第二个参数指示转换类型，OpenCV 中有超过 150 个颜色空间转换，这里我们使用的是彩色转灰度 `cv2.COLOR_BGR2GRAY`。

`os.get_terminal_size()` 方法返回当前终端的列数（宽），行数（高）。这里我们将 `fill` 参数设置为 `True`，未设置 `wrap` 参数，其值为默认的 `False`。在终端里如果打印的字符超过一行的宽度，终端会自动进行显示上的换行。

最后别忘了用 `cap.release()` 释放资源。

然后是 `play()` 方法，这就要接着之前说了，要想终端不在播放字符动画后充满没用的字符，可以使用光标定位转义编码。

我们可以这样：每输出一帧，就将光标移动到播放开始处，下一帧会从这个位置输出，并自动覆盖掉之前的内容，如此往复循环，播放完毕时，清除输出的最后一帧，这样终端就不会被字符画挤满了。

这里是一系列用来定位光标的转义编码（某些终端不支持一些转义编码），引自 *The Linux Command Line*：

| 转义编码  | 行动                                           |
| --------- | ---------------------------------------------- |
| \033[l;cH | 把光标移到第 l 行，第 c 列。                   |
| \033[nA   | 把光标向上移动 n 行。                          |
| \033[nB   | 把光标向下移动 n 行。                          |
| \033[nC   | 把光标向前移动 n 个字符。                      |
| \033[nD   | 把光标向后移动 n 个字符。                      |
| \033[2J   | 清空屏幕，把光标移到左上角（第零行，第零列）。 |
| \033[K    | 清空从光标位置到当前行末的内容。               |
| \033[s    | 存储当前光标位置。                             |
| \033[u    | 唤醒之前存储的光标位置。                       |

还有一个问题，如何在中途停止播放？当然你可以按 `Ctrl + C`，但这样程序是没办法做扫尾工作的，终端会留下一堆没用的乱七八糟的字符。

我们这样设计，字符动画开始播放时启动一个守护线程，进程启动时便开始等待用户输入，一旦接收到输入便停止播放字符动画。

这里有两个地方需要注意：

1. 不要使用 `input()` 方法接收字符输入
2. 不能使用普通线程

对于第一点，如果是想按任意字符终止播放的话，那么就不应该使用 `input()`，否则要么你按回车停止播放，要么按其他字符再敲回车停止播放，总而言之，使用 `input()` 并不舒服。最好的办法是，使用类似于 C 语言中的 getchar() 方法，然而 python 并没有提供类似方法，这在后面的代码中会给出替代方案。

对于第二点，我们要明白如果任何一个派生线程仍在运行中，主线程是不会退出的，除非派生线程被设定为守护线程。所以使用普通线程的话，若用户并没有在中途停止播放，等到播放完毕后，这个线程会永远的运行下去，直到用户输入任意字符。如果我们可以在播放完毕时手动 kill 掉这个派生线程，这也不是问题，然而 python 并没有提供 kill 掉线程的方法。所以，只能把这个派生线程设为守护线程。等主线程退出后，程序只剩下一个守护线程在运行，守护线程会自动被 kill 掉，程序退出。

下面类 `play()` 方法的代码：

```python
def play(self, stream = 1):
    # Bug:
    # 光标定位转义编码不兼容 Windows
    if not self.charVideo:
        return
    if stream == 1 and os.isatty(sys.stdout.fileno()):
        self.streamOut = sys.stdout.write
        self.streamFlush = sys.stdout.flush
    elif stream == 2 and os.isatty(sys.stderr.fileno()):
        self.streamOut = sys.stderr.write
        self.streamFlush = sys.stderr.flush
    elif hasattr(stream, 'write'):
        self.streamOut = stream.write
        self.streamFlush = stream.flush
    
    old_settings = None
    breakflag = None
    # 获得标准输入的文件描述符
    fd = sys.stdin.fileno()

    def getChar():
        nonlocal breakflag
        nonlocal old_settings
        # 保存标准输入的属性
        old_settings = termios.tcgetattr(fd)
        # 设置标准输入为原始模式
        tty.setraw(sys.stdin.fileno())
        # 读取一个字符
        ch = sys.stdin.read(1)
        breakflag = True if ch else False

    # 创建线程
    getchar = threading.Thread(target=getChar)
    # 设置为守护线程
    getchar.daemon = True
    # 启动守护线程
    getchar.start()
    # 输出的字符画行数
    rows = len(self.charVideo[0])//os.get_terminal_size()[0]
    for frame in self.charVideo:
        # 接收到输入则退出循环
        if breakflag is True:
            break
        self.streamOut(frame)
        self.streamFlush()
        time.sleep(self.timeInterval)
        # 共 rows 行，光标上移 rows-1 行回到开始处
        self.streamOut('\033[{}A\r'.format(rows-1))
    # 恢复标准输入为原来的属性
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    # 光标下移 rows-1 行到最后一行，清空最后一行
    self.streamOut('\033[{}B\033[K'.format(rows-1))
    # 清空最后一帧的所有行（从倒数第二行起）
    for i in range(rows-1):
        # 光标上移一行
        self.streamOut('\033[1A')
        # 清空光标所在行
        self.streamOut('\r\033[K')
    info = 'User interrupt!\n' if breakflag else 'Finished!\n'
    self.streamOut(info)
```

一些函数的文档链接：

> `termios.tcgetattr(fd)`、`termios.tcsetattr(fd, when, attributes)`：[链接](https://docs.python.org/3/library/termios.html?highlight=tcsetattr#termios.tcgetattr)
>
> `tty.setraw(fd, when=termios.TCSAFLUSH)`：[链接](https://docs.python.org/3/library/tty.html?highlight=setraw#tty.setraw)

`V2Char` 类的完整代码如下：

```python
class V2Char(CharFrame):

    charVideo = []
    timeInterval = 0.033

    def __init__(self, path):
        if path.endswith('txt'):
            self.load(path)
        else:
            self.genCharVideo(path)

    def genCharVideo(self, filepath):
        self.charVideo = []
        cap = cv2.VideoCapture(filepath)
        self.timeInterval = round(1/cap.get(5), 3)
        nf = int(cap.get(7))
        print('Generate char video, please wait...')
        for i in pyprind.prog_bar(range(nf)):
            rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
            frame = self.convert(rawFrame, os.get_terminal_size(), fill=True)
            self.charVideo.append(frame)
        cap.release()

    def export(self, filepath):
        if not self.charVideo:
            return
        with open(filepath,'w') as f:
            for frame in self.charVideo:
                # 加一个换行符用以分隔每一帧
                f.write(frame + '\n')

    def load(self, filepath):
        self.charVideo = []
        # 一行即为一帧
        for i in  open(filepath):
            self.charVideo.append(i[:-1])

    def play(self, stream = 1):
        # Bug:
        # 光标定位转义编码不兼容 Windows
        if not self.charVideo:
            return
        if stream == 1 and os.isatty(sys.stdout.fileno()):
            self.streamOut = sys.stdout.write
            self.streamFlush = sys.stdout.flush
        elif stream == 2 and os.isatty(sys.stderr.fileno()):
            self.streamOut = sys.stderr.write
            self.streamFlush = sys.stderr.flush
        elif hasattr(stream, 'write'):
            self.streamOut = stream.write
            self.streamFlush = stream.flush
        
        old_settings = None
        breakflag = None
        # 获得标准输入的文件描述符
        fd = sys.stdin.fileno()

        def getChar():
            nonlocal breakflag
            nonlocal old_settings
            # 保存标准输入的属性
            old_settings = termios.tcgetattr(fd)
            # 设置标准输入为原始模式
            tty.setraw(sys.stdin.fileno())
            # 读取一个字符
            ch = sys.stdin.read(1)
            breakflag = True if ch else False

        # 创建线程
        getchar = threading.Thread(target=getChar)
        # 设置为守护线程
        getchar.daemon = True
        # 启动守护线程
        getchar.start()
        # 输出的字符画行数
        rows = len(self.charVideo[0])//os.get_terminal_size()[0]
        for frame in self.charVideo:
            # 接收到输入则退出循环
            if breakflag is True:
                break
            self.streamOut(frame)
            self.streamFlush()
            time.sleep(self.timeInterval)
            # 共 rows 行，光标上移 rows-1 行回到开始处
            self.streamOut('\033[{}A\r'.format(rows-1))
        # 恢复标准输入为原来的属性
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        # 光标下移 rows-1 行到最后一行，清空最后一行
        self.streamOut('\033[{}B\033[K'.format(rows-1))
        # 清空最后一帧的所有行（从倒数第二行起）
        for i in range(rows-1):
            # 光标上移一行
            self.streamOut('\033[1A')
            # 清空光标所在行
            self.streamOut('\r\033[K')
        info = 'User interrupt!\n' if breakflag else 'Finished!\n'
        self.streamOut(info)
```



### 测试效果

把下面的代码键入到之前的代码后面，这份代码就可以用做视频转字符画的脚本文件了。

```python
if __name__ == '__main__':
    import argparse
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        help='Video file or charvideo file')
    parser.add_argument('-e', '--export', nargs = '?', const = 'charvideo.txt',
                        help='Export charvideo file')
    # 获取参数
    args = parser.parse_args()
    v2char = V2Char(args.file)
    if args.export:
        v2char.export(args.export)
    v2char.play()
```

用如下命令把测试用视频下载下来：

```sh
$ cd /home/shiyanlou/Code
$ wget http://labfile.oss.aliyuncs.com/courses/637/BadApple.mp4
```

输入如下命令将 `BadApple.mp4` 文件转为字符动画并导出为文件，同时播放转换后的字符动画（转码过程可能需要几分钟的时间，请耐心等待）。

```sh
$ python3 CLIPlayVideo.py BadApple.mp4 -e
```

之后再次播放不必重新转换一次，可以直接读取导出的字符画，假设这个文件是 `charvideo.txt`：

```sh
$ python3 CLIPlayVideo.py charvideo.txt
```

执行生成的文档如下：

![2.3-1](https://doc.shiyanlou.com/document-uid600404labid2102timestamp1531190484216.png)



### 附件：

完整代码：

可以直接把代码下载下来：

```sh
$ wget http://labfile.oss.aliyuncs.com/courses/637/CLIPlayVideo.py
```

下面贴出了完整的代码：

```python
import sys
import os
import time
import threading
import termios
import tty
import cv2
import pyprind


class CharFrame:

    ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

    # 像素映射到字符
    def pixelToChar(self, luminance):
        return self.ascii_char[int(luminance/256*len(self.ascii_char))]

    # 将普通帧转为 ASCII 字符帧
    def convert(self, img, limitSize=-1, fill=False, wrap=False):
        if limitSize != -1 and (img.shape[0] > limitSize[1] or img.shape[1] > limitSize[0]):
            img = cv2.resize(img, limitSize, interpolation=cv2.INTER_AREA)
        ascii_frame = ''
        blank = ''
        if fill:
            blank += ' '*(limitSize[0]-img.shape[1])
        if wrap:
            blank += '\n'
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                ascii_frame += self.pixelToChar(img[i,j])
            ascii_frame += blank
        return ascii_frame


class I2Char(CharFrame):

    result = None

    def __init__(self, path, limitSize=-1, fill=False, wrap=False):
        self.genCharImage(path, limitSize, fill, wrap)

    def genCharImage(self, path, limitSize=-1, fill=False, wrap=False):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return
        self.result = self.convert(img, limitSize, fill, wrap)

    def show(self, stream = 2):
        if self.result is None:
            return
        if stream == 1 and os.isatty(sys.stdout.fileno()):
            self.streamOut = sys.stdout.write
            self.streamFlush = sys.stdout.flush
        elif stream == 2 and os.isatty(sys.stderr.fileno()):
            self.streamOut = sys.stderr.write
            self.streamFlush = sys.stderr.flush
        elif hasattr(stream, 'write'):
            self.streamOut = stream.write
            self.streamFlush = stream.flush
        self.streamOut(self.result)
        self.streamFlush()
        self.streamOut('\n')


class V2Char(CharFrame):

    charVideo = []
    timeInterval = 0.033

    def __init__(self, path):
        if path.endswith('txt'):
            self.load(path)
        else:
            self.genCharVideo(path)

    def genCharVideo(self, filepath):
        self.charVideo = []
        cap = cv2.VideoCapture(filepath)
        self.timeInterval = round(1/cap.get(5), 3)
        nf = int(cap.get(7))
        print('Generate char video, please wait...')
        for i in pyprind.prog_bar(range(nf)):
            rawFrame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY)
            frame = self.convert(rawFrame, os.get_terminal_size(), fill=True)
            self.charVideo.append(frame)
        cap.release()

    def export(self, filepath):
        if not self.charVideo:
            return
        with open(filepath,'w') as f:
            for frame in self.charVideo:
                # 加一个换行符用以分隔每一帧
                f.write(frame + '\n')

    def load(self, filepath):
        self.charVideo = []
        # 一行即为一帧
        for i in  open(filepath):
            self.charVideo.append(i[:-1])

    def play(self, stream = 1):
        # Bug:
        # 光标定位转义编码不兼容 Windows
        if not self.charVideo:
            return
        if stream == 1 and os.isatty(sys.stdout.fileno()):
            self.streamOut = sys.stdout.write
            self.streamFlush = sys.stdout.flush
        elif stream == 2 and os.isatty(sys.stderr.fileno()):
            self.streamOut = sys.stderr.write
            self.streamFlush = sys.stderr.flush
        elif hasattr(stream, 'write'):
            self.streamOut = stream.write
            self.streamFlush = stream.flush
        
        old_settings = None
        breakflag = None
        # 获得标准输入的文件描述符
        fd = sys.stdin.fileno()

        def getChar():
            nonlocal breakflag
            nonlocal old_settings
            # 保存标准输入的属性
            old_settings = termios.tcgetattr(fd)
            # 设置标准输入为原始模式
            tty.setraw(sys.stdin.fileno())
            # 读取一个字符
            ch = sys.stdin.read(1)
            breakflag = True if ch else False

        # 创建线程
        getchar = threading.Thread(target=getChar)
        # 设置为守护线程
        getchar.daemon = True
        # 启动守护线程
        getchar.start()
        # 输出的字符画行数
        rows = len(self.charVideo[0])//os.get_terminal_size()[0]
        for frame in self.charVideo:
            # 接收到输入则退出循环
            if breakflag is True:
                break
            self.streamOut(frame)
            self.streamFlush()
            time.sleep(self.timeInterval)
            # 共 rows 行，光标上移 rows-1 行回到开始处
            self.streamOut('\033[{}A\r'.format(rows-1))
        # 恢复标准输入为原来的属性
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        # 光标下移 rows-1 行到最后一行，清空最后一行
        self.streamOut('\033[{}B\033[K'.format(rows-1))
        # 清空最后一帧的所有行（从倒数第二行起）
        for i in range(rows-1):
            # 光标上移一行
            self.streamOut('\033[1A')
            # 清空光标所在行
            self.streamOut('\r\033[K')
        info = 'User interrupt!\n' if breakflag else 'Finished!\n'
        self.streamOut(info)

if __name__ == '__main__':
    import argparse
    # 设置命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        help='Video file or charvideo file')
    parser.add_argument('-e', '--export', nargs = '?', const = 'charvideo.txt',
                        help='Export charvideo file')
    # 获取参数
    args = parser.parse_args()
    v2char = V2Char(args.file)
    if args.export:
        v2char.export(args.export)
    v2char.play()
```



·