## shutter 截图工具

> ubunu 16.04 亲测可用

```bash
sudo apt install shutter
```

shortcut settings:

`settings` --> `keyboard`  --> `shortcuts`  -->  `custom shortcuts`

<img src="https://img-blog.csdnimg.cn/8579cd3e28034047af00fdc439f4798a.png" alt="image-20210810162720518" style="zoom:80%;" />





# SimpleScreenRecorder

### 1. 安装SimpleScreenRecorder
**按Ctrl+Alt+T打开终端**


添加源：```sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder```

更新源：`sudo apt-get update`

安装：`sudo apt-get install simplescreenrecorder`

### 2. 打开软件
- 点击左上角启动器，在查找框输入：sim

- 点击SimpleScreenRecorder

PS：也可以把SimpleScreenRecorder拖到桌面快捷方式，方便以后打开

### 3. 软件介绍

大概意思就是说，推荐直接默认设置使用，当然也可以自己设置，如果需要了解更多，可以到他们的网站查看，不过这与我们使用软件无关，直接点击底部的continue

### 4. 录制窗口设置



- 默认的情况下，是所有屏幕全屏录制，30FPS

- video input下面4个选项

  - 第一个是全屏录制，右边的选项，第一个是所有显示器，下面他选项是针对某个显示器

  - 第二个是固定的坐标范围录制，比如屏幕的某一部分位置

  - 第三个是跟随鼠标录制，比如设定一个长度与宽度，鼠标去到那，录制的范围就跟到哪

  - 第四个是录制openGL应用

- Frame rate是录制的帧率，希望观看流畅尽量设置高点（一般显示器60帧，别超过这个数字），帧数高，视频体积也相对增大

- Scald video是把视频压缩到指定尺寸，一般不推荐使用

- Record cursor是记录鼠标，建议使用音频默认可以了

- 点击continue

### 5. 选择画质

画质有几个预设的选项

- high quality intermediate：高清视频

- Live Stream（1000kbps）：直播流，码率为1000kbps

- Live Stream（2000kbps）：直播流，码率为2000kbps

- Live Stream（3000kbps）：直播流，码率为3000kbps

- 	YouTube：高质量视频

除了预选择，也可以自己设置画质，下面会说到

### 6. 选择视频存储位置

- 点击browse浏览文件夹，选择一个文件夹以及输入默认名称，点击保存

- 视频的命名方式是，你预设的名称+日期时间

### 7. 设置视频格式、编码、码率，帧率，设置声音格式、码率
**Video：**

   - Container：封装视频的格式有MKV，MP4等

   - Codec：编码方式有很多，推荐H264，高压缩，省硬盘空间

   - Constant rate factor：范围0-51，数字越低画质越好

   - Preset：设置码率，这些选项里面，越往上越高（码率高细节好）

**Audio：**

   - Codec：一般是MP3或者AAC

  -  Bit rate：一般128或者192，麦克风不行的话设置太高也是浪费存储空间

设置完成后，点击底部的continue

### 8. 录制视频

设置完成后，到了开始录制视频这一步

顶部的Start recording就是开始录制视频，点击就开始录制了

中间的Start preview就是开始预览，比如把当前录制内容显示出来

底部的Save recording就是结束当前录制并且保存

另外，通过点击托盘栏的软件图标，也是可以快速开始录制与保存

### over！！！
