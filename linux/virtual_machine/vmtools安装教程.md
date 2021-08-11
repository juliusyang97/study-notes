 > 1. VMtools能够实现主机和虚拟机之间的文件复制粘贴，调整虚拟机使其满屏
 >
 > 2. 安装vmtools时，虚拟机系统是要保持开机状态的（本文是Ubuntu16.04）

1. 点击重新安装vmtools
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210611152415105.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTM5MjA4MQ==,size_16,color_FFFFFF,t_70)
2. 如果正常会弹出以下界面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210611153535235.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTM5MjA4MQ==,size_16,color_FFFFFF,t_70)

3. 打开终端，可以看到当前路径，将压缩包解压到制定路径下
```
sudo tar zxvf VMwareTools-10.3.2-9925305.tar.gz -C /home
```
切换路径到刚解压的路径，可以看到解压后的文件
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210611153756598.png)

4. 执行`vmware-install.pl`文件
```
sudo ./vmware-install.pl 
```
5. 安装完成后重启虚拟机即可，，，


试试虚拟机和主机之间互相拖动文件能复制就说明成功了