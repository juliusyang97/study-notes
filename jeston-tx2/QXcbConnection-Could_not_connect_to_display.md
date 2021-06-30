> 远程连接无法显示，报错如下：QXcbConnection: Could not connect to display

解决方案：修改远程端环境变量

```
vim ~/.bashrc
```

```
export QT_QPA_PLATFORM='offscreen'
```

```
source ~/.bashrc
```

