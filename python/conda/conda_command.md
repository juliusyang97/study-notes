[conda更换国内源方法链接](./conda更换国内源的方法.md)

1. 查看当前已有环境
```
conda info --envs
```
或者
```
conda env list
```
2. 创建新环境
```
conda create -n env_name python=3.6
# 同时安装必要的包
conda create -n env_name numpy matplotlib python=3.6
```

3. 删除已有环境
```
conda remove -n env_name --all
```
4. 环境切换
```
# linux/Mac下需要使用
#source activate env_name
conda activate env_name
#Windows下使用
activate env_name
#退出环境
deactivate env_name
```

5. 查看已安装的package
```
conda list
# 指定查看某环境下安装的package
conda list -n env_name
```

6. 使用conda安装package
```
conda install numpy
```
7. 卸载package
```
conda remove numpy 
```
8. 查找package
```
conda search  numpy
```
9. 更新package
```
conda update numpy
```

 

