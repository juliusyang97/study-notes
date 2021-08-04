打开gazebo的时候会发现一直处于黑屏这种状态，这是因为model库加载不正确导致的。
```bash
 cd ~/.gazebo/
 mkdir -p models
 cd ~/.gazebo/models/
 wget http://file.ncnynl.com/ros/gazebo_models.txt
 wget -i gazebo_models.txt
 ls model.tar.g* | xargs -n1 tar xzvf
```

如果还是黑屏 可以使用如下两条指令
```bash
killall gzserver
killall gzclient
```

