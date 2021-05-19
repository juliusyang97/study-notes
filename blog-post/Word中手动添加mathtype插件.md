> 我们在已经安装好Word和mathtype的情况下，Word中没有显示mathtype或者Word软件重装了，mathtype软件没有动，这时我们可以通过手动添加的方式在Word中加入mathtype插件

1. 首先找到Word中的受信任位置
点击`文件` → `选项` → `信任中心设置` → `受信任位置`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210519204558540.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTM5MjA4MQ==,size_16,color_FFFFFF,t_70)
2. 找到你自己安装mathtype软件的路径，复制以下几个文件到刚开找到的那个`startup`文件夹中，注意自己安装的Word软件是64位还是32位，对应起来（我这是64位的，所以复制的文件都是名为`64`文件夹下的）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210519205057974.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTM5MjA4MQ==,size_16,color_FFFFFF,t_70)


![在这里插入图片描述](https://img-blog.csdnimg.cn/20210519205146949.png)


重启Word，OK！！！