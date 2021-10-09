> 问题描述：我安装的是Ubuntu和Windows双系统，原本是好的，可以正常进入选择系统的引导界面（应该是叫grub吧）。然而，它崩了，不见了，开机直接进入Windows，没有引导了，，，，
> 通过查阅资料，找到了大致一下几种解决办法，这里直接上**结论，我这里成功的方法是方法二：在Windows下成功解决问题的**



### 方法一：
> 这种方法是博客中说的最多的一种方法，搜索引擎随便一搜基本都是这种方法

大致解决思路：
1. 查看BIOS，把安全启动关掉；
2. 通过制作的安装盘进入`try ...`这个选项，就是不安装Ubuntu，先进入系统的那个选项，之后安装一个引导修复软件，这种方法我现在测试好像失效了（2021年10月09日14:59:06），安装软件显示找不到了已经，方法也记录一下吧
```
# 添加软件源
sudo add-apt-repository ppa:yannubuntu/boot-repair
sudo apt update
# 安装boot-repair
sudo apt install -y boot-repair
boot-repair

# 修复之后跟新下grub
sudo update-grub
sudo update-grub2
```

### 方法二:
这种方法的解决思路，我的理解就通过Windows吧Ubuntu的应到加载进来

方法：
用管理员打开`powershell`，执行以下命令，显示执行成功即可，重启出现了熟悉的grub引导界面
```powershell
bcdedit /set "{bootmgr}" path \EFI\ubuntu\grubx64.efi
```
***reference:https://lkevin98.gitee.io/blog/posts/60319***

附：使用`Boot from file`功能直接引导
进入BIOS -> `Boot Menu` -> `Boot from file` -> `EFI` -> `Boot` -> `bootx64.efi`
 我觉得这种引导方式应该也是第二种解决方案的原理有一点类似吧

