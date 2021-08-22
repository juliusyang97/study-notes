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

