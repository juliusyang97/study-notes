[rosdep update 超时失败2021最新解决方法_Kenny_GuanHua的博客-CSDN博客](https://blog.csdn.net/Kenny_GuanHua/article/details/116845781)

[解决ROS系统 rosdep update超时问题的新方法_leida_wt的博客-CSDN博客_rosdep update 超时](https://blog.csdn.net/leida_wt/article/details/115120940)





参考 leida_wt 的方法，网站https://ghproxy.com/支持github的资源代理，非常好用，我们将用此代理加速rosdep对Github的访问，进而解决rosdep update失败问题。

我们要做的，是在rosdep的若干个脚本文件中，把 https://ghproxy.com/ 添加到相应URL前面即可。

1.首先修改rosdep下载资源的脚本文件：/usr/lib/python2.7/dist-packages/rosdep2/sources_list.py，把以下行添加到脚本中的download_rosdep_data()函数中，以应用代理服务：

url="https://ghproxy.com/"+url




2.然后，用同样的方法修改/usr/lib/python2.7/dist-packages/rosdistro/__init__.py里面的DEFAULT_INDEX_URL参数，如下：

DEFAULT_INDEX_URL = 'https://ghproxy.com/https://raw.githubusercontent.com/ros/rosdistro/master/index-v4.yaml'
3.接着，以下4个文件中也使用了“raw.githubusercontent.com”网址，同样的方法把“https://ghproxy.com/”添加到网址前：

/usr/lib/python2.7/dist-packages/rosdep2/gbpdistro_support.py 36行
/usr/lib/python2.7/dist-packages/rosdep2/sources_list.py 72行
/usr/lib/python2.7/dist-packages/rosdep2/rep3.py	39行
/usr/lib/python2.7/dist-packages/rosdistro/manifest_provider/github.py 68行 119行
4.最后，在 /usr/lib/python2.7/dist-packages/rosdep2/gbpdistro_support.py 的第204行添加如下代码：

gbpdistro_url = "https://ghproxy.com/" + gbpdistro_url



大功告成，现在你可以愉快地执行 rosdep update 啦！预祝一把过。
————————————————
版权声明：本文为CSDN博主「马赫_WGH」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Kenny_GuanHua/article/details/116845781