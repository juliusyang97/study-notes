>  关于课程中的一些记录



## ROS package install 

1. 如果ros安装了一个功能包之后，`tab`补全找不到刚装的包，这时需要做以下工作:

```bash
rospack profile
```

说明：在环境配置都做好的情况下，这个工作的本质就像是对系统的索引做一次强制刷新（或者等一会儿应该也会能检索到）





## bashrc settings about ROS

1. 如果有两个以上工作空间的话，可能会出现一个覆盖另一个的情况，这时最要做以下工作即可：

```bash
source /opt/ros/kinetic/setup.bash
source ~/catkin_ws/devel/setup.bash --extend
source ~/catkin_ws_1/devel/setup.bash --extend
```

说明：想关闭哪个workspace只需注释掉对应行即可；





