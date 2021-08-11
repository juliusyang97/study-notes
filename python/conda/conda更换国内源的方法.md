[conda常用命令汇总](python/conda/conda_command.md)

1. 添加清华源
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
#设置搜索时显示通道地址
conda config --set show_channel_urls yes
```

2. 添加中科大源
```
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```
3. 查看
```
#查看当前的 cofig 
conda config --show

#查看添加的镜像：
conda config --get channels
```
4. 删除源
```
conda config --remove-key channels
```
