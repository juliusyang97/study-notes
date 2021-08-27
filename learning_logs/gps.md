田老师您好！

​	我是前段时间我们在上海线下睿慕课举办的《ros无人车开发实践》学员杨军奇，我有一些问题想请教一下您。我这边现在有一个GPS，但是我不知道怎么把GPS能和车上目前的设备结合起来，用GPS来进行导航，就好比是我现在用激光雷达先建立地图，然后利用一些算法去导航。这个过程在GPS上我该如何实现呢，我应该找一些什么算法，我该从什么地方去下手把GPS和车联系起来（或者说能够让车用GPS跑起来），最近我查了一些资料，但是感觉一团乱，不知道如何下手了，希望能得到您的指导。





> 无人车平台：Ubuntu16.04    kinetic  

>  无人车目前可以使用gmaping、amcl

需求：现在有一个华测的CGI-410GPS，想使用GPS来进行室外导航。

我目前尝试做了以下工作：

1. 通过串口（RS232）转usb把GPS连接到无人车主机
2. 无人车主机安装了`nmea_navsat_driver` 
3. 运行下列命令查看GPS数据：

```bash
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyUSB3 _baud:=230400
```

4. 

```bash
rostopic echo /fix
```

输出数据如下：

```bash
header: 
  seq: 134
  stamp: 
    secs: 1629641773
    nsecs: 190377950
  frame_id: "/gps"
status: 
  status: -1
  service: 1
latitude: nan
longitude: nan
altitude: nan
position_covariance: [9998.0001, 0.0, 0.0, 0.0, 9998.0001, 0.0, 0.0, 0.0, 39992.0004]
position_covariance_type: 1
---
header: 
  seq: 135
  stamp: 
    secs: 1629641773
    nsecs: 193670034
  frame_id: "/gps"
status: 
  status: -1
  service: 1
latitude: nan
longitude: nan
altitude: nan
position_covariance: [9998.0001, 0.0, 0.0, 0.0, 9998.0001, 0.0, 0.0, 0.0, 39992.0004]
position_covariance_type: 1
---
header: 
  seq: 136
  stamp: 
    secs: 1629641773
    nsecs: 196938037
  frame_id: "/gps"
status: 
  status: -1
  service: 1
latitude: nan
longitude: nan
altitude: nan
position_covariance: [9998.0001, 0.0, 0.0, 0.0, 9998.0001, 0.0, 0.0, 0.0, 39992.0004]
position_covariance_type: 1
---
```

5. topic

```
julius@julius-ubuntu: ~$ rostopic list 
/battery
/bulldog_velocity_controller/cmd_vel
/bulldog_velocity_controller/odom
/bulldog_velocity_controller/parameter_descriptions
/bulldog_velocity_controller/parameter_updates
/cmd_vel
/diagnostics
/diagnostics_agg
/diagnostics_toplevel_state
/e_stop
/fix
/imu/data
/joint_states
/joy
/joy/set_feedback
/joy_teleop/cmd_vel
/odometry/filtered
/platform_control/cmd_vel
/rosout
/rosout_agg
/set_pose
/tf
/tf_static
/time_reference
/twist_marker_server/cmd_vel
/twist_marker_server/feedback
/twist_marker_server/update
/twist_marker_server/update_full
/vel
```
6. node

```
julius@julius-ubuntu: ~$ rosnode list 
/bulldog_driver
/controller_spawner
/diagnostic_aggregator
/ekf_localization
/imu_driver
/joy_node
/nmea_serial_driver
/robot_state_publisher
/rosout
/teleop_twist_joy
/twist_marker_server
/twist_mux

```





