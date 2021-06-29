# 多机通信配置

## 1. 保证各模块通电正常

## 2. 主机Network设置：

![image-20210629212814948](/home/julius/.config/Typora/typora-user-images/image-20210629212814948.png)

```
Settings --> Wired --> options --> IPv4 Settings ##(Method: Manual, Adress & NetMask)
```

`eg： 192.168.1.30 ,    255.255.255.0`

## 3. Ros `Start.sh` setting:

> path is `/opt/ros/scripts/start.sh`

add :  (主机IP)

```bash
export ROS_MASTER_URI=http://192.168.1.30:11311
export ROS_IP=192.168.1.30
```

start.sh as follows:

```
#!/bin/bash


if [ -f /opt/ros/kinetic/setup.bash ];then
     source /opt/ros/kinetic/setup.bash
fi

if [ -f /home/shansu/catkin_ws/devel/setup.bash ];then
     source /home/shansu/catkin_ws/devel/setup.bash
fi
export ROS_MASTER_URI=http://192.168.1.30:11311
export ROS_IP=192.168.1.30
echo "ROS environment is Ready"
sleep 3
roslaunch bulldog_driver bulldog_base.launch

```

## 4. 主、从机`hosts`配置

> path is `/etc/hosts`

master： add slave address  

`eg: 192.168.1.134	nvidia-desktop`   #(中间用tab键隔开)

slave: add master address

`eg: 192.168.1.30	bulldog`

## 5. 配置自启动文件

> path is `etc/rc.local`

add ROS `start.sh` to `rc.local`

eg: 

```bash
# ......
/opt/ros/scripts/start.sh
exit 0
```

## 6. 配置从机环境变量`.bashrc`

```
export ROS_MASTER_URI=http://192.168.1.30:11311
export ROS_IP=192.168.1.134
```

```bash
source ~/.bashrc
```







## others:

1. kill master

   ```bash
   sudo killal -9 rosmaster
   ```

   

2. 手柄调教工具

   ```bash
   sudo apt install jstest-gtk
   
   jstest-gtk
   ```

   