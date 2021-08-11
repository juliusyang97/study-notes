[使用方法 · v2rayA/v2rayA Wiki (github.com)](https://github.com/v2rayA/v2rayA/wiki/使用方法)

安装 V2Ray 内核 / Xray 内核
使用 systemd 的 Linux 发行版

V2Ray 安装参考：https://github.com/v2fly/fhs-install-v2ray

Xray 安装参考：https://github.com/XTLS/Xray-install

安装后可以关掉服务，因为v2rayA不依赖于该systemd服务。


```bash 
sudo systemctl disable v2ray --now ### Xray 需要替换服务为 xray
```