1. 将ros中的gps_msg数据导入google earth显示轨迹 : https://blog.csdn.net/datase/article/details/79061219



2. ubuntu 同时使用无线网卡和有线网卡：https://blog.csdn.net/huohongpeng/article/details/78608671#commentBox

     




### 关于网络连接的问题

> 1. 虚拟机无法连接无人车网络有线：首先直接用windows宿主机连接无人车WiFi（实测只需先断开宿主机连接的WiFi，尝试虚拟机连接无人车，连接成功之后宿主机再连接WiFi即可），然后虚拟机顺利`ssh`连接无人车，之后断开WiFi（有线还能保持ssh连接正常），WiFi连接外网
>
> 2. 如果需要在虚拟机中使用外网，得把和无人车连接的有线网络拔掉，虚拟机才可以正常上网。
>
> 3. 无人车需要上外网的话，可以通过WiFi，或者手机USB分享网络都可以。
>
>     ```bash
>     sudo nmcli device wifi connect WIFI名称 password WIFI密码
>     ```
>
>     



3. ROS 之 2d Nav goal不工作:https://blog.csdn.net/weixin_40639095/article/details/108253724





ROS-使用命令发布导航目标点（publish point）https://blog.csdn.net/qq_45281711/article/details/107559108



https://github.com/ydsf16/imu_gps_localization



### 尝试1：

[基于ROS的室外导航尝试_Nickyang的博客-CSDN博客](https://blog.csdn.net/ANyang5/article/details/115447061)

[wulifzd/get_gps (github.com)](https://github.com/wulifzd/get_gps)

[gps_goal - 罗斯维基 (ros.org)](http://wiki.ros.org/gps_goal)

[移动机器人传感器——GNSS](https://blog.csdn.net/Kalenee/article/details/114671891)

[GPS在ROS中的测试和使用](http://community.bwbot.org/topic/718/gps%E5%9C%A8ros%E4%B8%AD%E7%9A%84%E6%B5%8B%E8%AF%95%E5%92%8C%E4%BD%BF%E7%94%A8)

[gps + navigation - ROS Answers: Open Source Q&A Forum](https://answers.ros.org/question/12663/gps-navigation/)

[CesMak](https://github.com/CesMak)/**[rviz_maps](https://github.com/CesMak/rviz_maps)**

[ArduSimple RTK - ROS 集成](https://msadowski.github.io/ardusimple-ros-integration/)



A BETTER SOLUTION FOR GPS WAYPOINT NAVIGATION: https://clearpathrobotics.com/blog/2018/06/better-solution-for-gps-waypoint-navigation/

[sigmaai](https://github.com/sigmaai)/**[self-driving-golf-cart](https://github.com/sigmaai/self-driving-golf-cart)**  --> [GPS Localization with ROS, rviz and OSM – Neil Nie](https://neilnie.com/2018/05/10/gps-localization-with-ros-rviz-and-osm/#:~:text=GPS Localization with ROS%2C rviz and OSM. When,crucial to self-driving vehicles%2C which requires incredible precision.)

**[ArghyaChatterjee](https://github.com/ArghyaChatterjee)/[gps-waypoint-based-autonomous-navigation-in-ros](https://github.com/ArghyaChatterjee/gps-waypoint-based-autonomous-navigation-in-ros)**

[husky](https://github.com/husky)/[husky](https://github.com/husky/husky)

[danielsnider](https://github.com/danielsnider)/**[MapViz-Tile-Map-Google-Maps-Satellite](https://github.com/danielsnider/MapViz-Tile-Map-Google-Maps-Satellite)**

https://github.com/nickcharron/waypoint_nav

室外自动导航车：https://blog.csdn.net/z824074989y/category_9117770.html



> 博客园博主FlyingGod_ROS -->  https://www.cnblogs.com/flyinggod/category/1222137.html
>
>  [ROS costmap代价地图](https://www.cnblogs.com/flyinggod/p/12742889.html)







Map update loop missed its desired rate of 1.0000Hz... the loop actually took 5.1845 seconds

Datum UTM coordinate is (382166.057558, 3994866.939381)

Datum (latitude, longitude, altitude) is (36.091291, 103.691113, 1488.993000)

Deleting Nodes: 0 1 2 3 4 5 6 7 8 10 11 12 13 14 15 16 18 20 21 22 24 25 26 27 29 30 32 34 38 39 40 41 42 43 45 47 48 49 50 52 53 54 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 73 74 75 76 77 78 79 Done





ROS联合webots实战案例(五)导航功能包入门1：https://www.guyuehome.com/23791
ROS联合webots实战案例(五)导航功能包入门2：https://www.guyuehome.com/23792

up：锡城筱凯 --> [古月居 - ROS机器人知识分享社区 (guyuehome.com)](https://www.guyuehome.com/author/61075b32c7cf0)



搭建基于ROS的自主机器人平台https://leiyiming.com/2016/05/05/tank1/





## 机器人研发平台

http://www.clearpathcn.com/





### /opt/ros文件结构：

**①bin文件夹**：放置一些具体的可执行的程序，在ros的bin文件夹下面保存的都是ros系统和一些功能包给我们提供的可以直接执行的命令，可以在终端下面执行这些命令。

注：在执行bin文件夹下面的命令时，必须先设置环境变量，不然系统无法找到bin文件夹。

**②etc文件夹**：ros相关的配置文件(用的相对少)

**③include文件夹**：包含所有通过命令行、通过终端安装的功能包的代码头文件。

**④lib文件夹**：包含通过终端安装功能包的可执行程序，也就是节点。功能包中的节点，通过运行节点，来启动相应功能包里面的功能。

**⑤share文件夹**:里面有很多通过终端安装的功能包，保存的是功能包里面接口的一些具体信息，接口包含话题、服务、action等。





