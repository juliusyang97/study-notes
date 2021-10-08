### ROS 机器人如何使用GPS定位导航

> reference:http://www.yzrobot.cn/newsshow-16-121-1.html

发布时间：2018-10-29

#### 1. GPS简述



GPS定位已经是非常普及的技术了，不夸张的说，现今社会几乎人人都在主动或被动的使用它。最最常见的应用案例就是智能手机了。现在每一款手机都内置有GPS定位功能，使用者可以随时知道自己所在的位置。

GPS的全称是“全球卫星定位系统”，目前投入商业应用的主要有四套选择：GPS 系统（美国）、BDS 系统（中国北斗）
、GLONASS 系统（俄罗斯）和伽利略卫星导航系统（欧盟）。

GPS就是利用设备接收到的组网卫星信号来计算出设备当前的准确的地理位置，实现原理并不神秘，想了解更多技术原理请百度一下，此处不再重述。

毋庸置疑，美国的GPS系统目前是完备和商用化最普及的首选系统，中国的北斗系统这几年发展迅猛，尽管定位精度和使用范围现在还稍逊于美国的GPS系统，但估计很快就要达到甚至超过美国。俄罗斯和欧盟的自主GPS系统由于受到经费预算成本的困扰，近期发展进步并不明显，因此用户数量有限，尚未全面普及。





#### 2. 机器人利用GPS模块来定位的可行性与局限性



GPS模块在户外机器的定位导航方面是一个最基本的配置。注意这里主要是针对在户外工作的机器人，若您的机器人是室内使用的，根本不会被允许到室外工作，那么GPS模块就没有任何价值了。因为建筑物的屋顶和墙体会把GPS卫星信号大幅度削弱，一般商用级别的GPS模块根本接收不到符合要求的信号。

是不是户外机器人搭载GPS模块，就可以精确知道自己的位置？是，也不是！说是，是因为在大尺度地图（比例尺一般为每厘米100米左右）上，普通商用经济款的GPS模块一般能达到的定位精度是20米~50米，在100米/厘米这个级别的地图上可以比较准确的知道机器人当前位置。说不是，是指在机器人工作区域的微尺度地图（一般是每厘米10米以下），GPS模块给出的位置误差范围太大，仅仅利用GPS模块算出来的经纬度坐标无法实现机器人的准确定位，当然更无法推算出机器人的准确运动方向。很遗憾，20米~50米的位置误差对机器人完成指定任务的应用来说是不可接受的。

有些人可能很好奇，为什么很多商用的GPS模块的技术参数上都写的是2.5米的精度，你这里却说是10~50米，是不是你用的GPS太LOW了？有过GPS模块使用经验的工程师会告诉你，没错！理论上标称2.5米的误差的普通商用经济款GPS模块，在实际应用中，10~50米的误差是非常正常的。产生这个误差的原因有很多，在此暂不展开。



#### 3. ROS机器人如何利用GPS模块来精确定位



看到上面的结论，是不是说GPS对机器人的定位导航作用不大？非也！现在的机器人绝对不只是搭载GPS这一种传感器，常见的机器人都配置有激光雷达、声纳雷达、视觉测距等短距离精确测距设备，利用这些设备，一方面机器人可以及时发现周围障碍物并及时躲避，另一方面机器人也可是利用这个写精确测距传感器来实现局部环境识别定位与导航。

很显然，利用GPS模块来实现20~50米范围内的粗略位置定位，再利用机器人搭载的短距离精确测距设备（声纳、激光雷达等等）来实现小范围的局部精确定位，这样就可以使户外机器人在任何大小尺度的地图范围内都可以准确定位了。





#### 4. GPS模块接收到的数据如何变成机器人工作地图的位置坐标



普通商用GPS模块输出的数据格式均符合NMEA0183标准，通过串口通讯，机器人可以获得的GPS数据实例如下：
$GNGGA,084852.000,2236.9453,N,11408.4790,E,1,05,3.1,89.7,M,0.0,M,,*48
$GNGLL,2236.9453,N,11408.4790,E,084852.000,A,A*4C
$GPGSA,A,3,10,18,31,,,,,,,,,,6.3,3.1,5.4*3E
$BDGSA,A,3,06,07,,,,,,,,,,,6.3,3.1,5.4*24
$GPGSV,3,1,09,10,78,325,24,12,36,064,,14,26,307,,18,67,146,27*71
$GPGSV,3,2,09,21,15,188,,24,13,043,,25,55,119,,31,36,247,30*7F
$GPGSV,3,3,09,32,42,334,*43
$BDGSV,1,1,02,06,68,055,27,07,82,211,31*6A
$GNRMC,084852.000,A,2236.9453,N,11408.4790,E,0.53,292.44,141216,,,A*75
$GNVTG,292.44,T,,M,0.53,N,0.98,K,A*2D
$GNZDA,084852.000,14,12,2016,00,00*48
$GPTXT,01,01,01,ANTENNA OK*35
数据里面有三种数据类型GN、GP、BD ，他们分别代表双模模式、GPS 模式、北斗模式
NMEA0183 协议 帧格式内容可以参考以下几个表格
(1) $GPGGA （GPS 定位信息）
(2) L $GPGLL （地理定位信息）
(3)A $GPGSA （当前卫星信息）
(4) $GPGSV （可见卫星信息）
(5) $GPRMC （最简定位信息）
(6) $GPVTG （地面速度信息）（7）天线状态输出
我们主要使用GPGGA（或GNGGA）这一帧的数据，具体分析如下：

![img](http://www.yzrobot.cn/uploads/image/20181029/1540777987.jpg)

1) UTC 时间，格式是 hhmmss.sss ，小数点后三位秒忽略，那就 08 点 48 分 52秒。UTC + 时区差 ＝ 本地时间时区差东为正，西为负。在此，把东八区时区差记为 +08， 所以北京时间是 16 点 48 分 5 秒

2) 收到的经纬度的数据格式是度分格式，实际使用中为了方便要换算成度+十进制小数，例如：
   纬度：ddmm.mmmm 北纬 2236.9453 22+(36.9453/60)= 22.615755
   经度：dddmm.mmmm 东经 11408.4790 114+(08.4790/60)=114.141317

3）第8项是衰减因子，这个数值代表的是误差水平。



机器人定位主要用经纬度和衰减因子这三个指标。经纬度用来定位，衰减因子用来计算出定位误差半径。

对于已经绘制好的机器人地图，ROS架构下用的最多的PGM格式的占位地图，由这种地图的定位是以米为单位的XY二维平面坐标系，这个坐标系和GPS提供的经纬度坐标系需要用至少两个点来标定转换才能互通，因此，当机器人使用二维PGM格式的占位地图来定位导航时，我们必须先选取PGM地图上的两个点作为标定参考点（通常选坐标原点和X轴上的最远距离点作为标定参考点），然后再记录下这两个标定点的经纬度数值，通过平面几何的三角函数计算出GPS经纬度坐标系和PGM地图坐标系之间的转换函数，这样就将GPS获得的经纬度数据与机器人的地图坐标一一对应起来



为了能让ROS机器人利用接收到的GPS信息进行定位导航这里需要编写两个专门的节点，一个用来读取GPS模块的帧信息，另一个用来把GPS信息转化为ROS地图坐标的节点，用C++或PYTHON可以比较容易的实现上述经纬度和PGM坐标

系之间的转换函数。



当然，普通商业用途的GPS模块转化来的坐标信息有10米~20米左右的精度误差，这一点就需要再ROS下的改良过的AMCL

节点来进行二次处理，才能精确的实现诸如巡检机器人、安防机器人等ROS架构机器人的精确定位与导航