1. 查看当前连接屏幕信息
```
xrandr
```
显示信息如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020070710491753.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTM5MjA4MQ==,size_16,color_FFFFFF,t_70)
我这里笔记本屏为`eDP-1-1`，外接屏为`HDMI-1-1`

2. 复制屏幕
```
xrandr --output HDMI-1-1 --same-as eDP-1-1 --auto
```
3. 右扩展屏幕（HDMI为eDP的右扩展屏）
```
xrandr --output HDMI-1-1 --right-of eDP-1-1 --auto 
```
			
4. 只显示副屏
```
xrandr --output HDMI-1-1 --auto --output eDP-1-1 --off 
```

5. 设置主副屏
我这里设置外扩屏为主屏幕，我把笔记本电脑放在了左边侧着，扩展屏当主屏幕
```
xrandr --output HDMI-1-1 --primary
```

6. 设置笔记本为左扩展屏
```
xrandr --output eDP-1-1 --left-of HDMI-1-1
```

