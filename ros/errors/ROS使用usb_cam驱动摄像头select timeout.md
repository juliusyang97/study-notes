> 问题描述：安装好ros usb_cam之后，启动报错如下：

```bash
[ERROR] [1628145296.402181976]: Cannot identify '/dev/video0': 2, No such file or directory
[usb_cam-1] process has died [pid 4035, exit code 1, cmd /opt/ros/melodic/lib/usb_cam/usb_cam_node __name:=usb_cam __log:=/home/yjq/.ros/log/72304fd4-f5b5-11eb-a1cf-000c29b89050/usb_cam-1.log].
log file: /home/yjq/.ros/log/72304fd4-f5b5-11eb-a1cf-000c29b89050/usb_cam-1*.log
```





解决方法：**把USB设置成3.0模式**

由于我这里使用的是虚拟机，所以在虚拟机设置里将USB兼容性设置为3.1问题就解决了



补充：

1. ros usb_cam的安装及启动命令：

```bash
sudo apt-get install ros-kinetic-usb-cam
roslaunch usb_cam usb_cam-test.launch
```

2. 使用usb_cam软件包调试usb摄像头  ---  博文教程：

    https://www.corvin.cn/535.html