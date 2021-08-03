> 问题描述：这两天想在Ubuntu上搞一个去探索世界的小软件（科学上网），Windows端使用的是v2rayN，所以就搞个一样的吧～～
> 找了一圈有个v2raya可以一干，那就搞

#### 开搞：
放上教程链接[V2ray Linux客户端v2rayA下载安装及使用教程 支持VMess/VLESS/SS/SSR/Trojan](https://v2xtls.org/v2ray-linux%e5%ae%a2%e6%88%b7%e7%ab%afv2raya%e4%b8%8b%e8%bd%bd%e5%ae%89%e8%a3%85%e5%8f%8a%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b-%e6%94%af%e6%8c%81vmess-vless-ss-ssr-trojan-pingtunnel/)
（这链接不靠谱，你问我为啥不靠谱？？？这都不知道就放弃吧，外面的世界你不配，嘿嘿）

1. 按照教程先把v2ray内核给装上，没问题，教程上有安装脚本
2. 安装v2raya客户端
有好几种方法，但是我都试了，没用，一个都没搞好，放弃了！！！！！放羊去了～～～


想想外面的世界多美好，怎么能放弃呢！！继续搞它

这个客户端安装大致可以用
1. 源码编译（failed）
2. 运行`xx.AppImage`，就是和Windows端`.exe`类似的东东（这玩意儿按道理，鼠标双击就能打开快乐的使用了，我也设置了`allow executing file as program`，然而我鼠标点坏了两个也点着没反应，放弃了）
3. 从软件源安装（加载源，搞了半天，key验证不过去，还搞个基啊）


3种方法没一个可行的，直接上解决方案吧，故事写不下去了，太长了～～～

**这里我最后用的是从软件源安装的方式：**
```
wget -qO - http://apt.v2raya.mzz.pub/key/public-key.asc | sudo apt-key add -
```
用以上命令添加源的时候一直报错：
```
gpg: no valid OpenPGP data found
```
apt update时的时候显示
```
W: GPG error: https://apt.v2raya.mzz.pub v2raya InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY F4FEBCD04F64D328
E: The repository 'http://apt.v2raya.mzz.pub v2raya InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
```
查了会资料大概应该是就是key验证不过去，，，，

最后看安装命令`wget -qO - http://apt.v2raya.mzz.pub/key/public-key.asc | sudo apt-key add -`，管道前面的下载秘钥文件，那我先把秘钥下载下来在添加，试了一下wget下载秘钥时命令没报错但是没反应也没有，按道理wget是会从远处下载个东西过来的，所以直接查看了下`http://apt.v2raya.mzz.pub/key/public-key.asc`这是个啥玩意，在网页端直接打开是个文件（问题找到了，就是这个文件没下载下来），手动下载下来，然后添加进去
```
sudo apt-key add public-key.asc
```
成功了，后续按教程即可


#### 可以快乐的玩耍了。。。。





