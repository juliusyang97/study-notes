ubuntu18.04按照wiki上安装步骤执行sudo rosdep init是出现
sudo: rosdep：找不到命令
原因：python-rosdep这个包没有装。
解决办法：
安装python-rosdep

```bash
sudo apt-get install python-rosdep
```

继续接下来的安装即可：

```bash
sudo rosdep init
rosdep update
```


