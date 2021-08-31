# Ubuntu连接WiFi

使用 NetworkManager 工具来管理网络，其在命令行下对应的命令是 nmcli，要连接WiFi，相关的命令如下：

- 查看网络设备列表

```bash
$ sudo nmcli dev
```

注意，如果列出的设备状态是 unmanaged 的，说明网络设备不受NetworkManager管理，你需要清空 /etc/network/interfaces下的网络设置,然后重启.

- 开启WiFi

```bash
$ sudo nmcli r wifi on
```

- 扫描附近的 WiFi 热点

```bash
$ sudo nmcli dev wifi
```

- 连接到指定的 WiFi 热点

```bash
$ sudo nmcli dev wifi connect "SSID" password "PASSWORD" ifname wlan0
```

请将 SSID和 PASSWORD 替换成实际的 WiFi名称和密码。

例如：

```bash
sudo nmcli device wifi connect WIFI名称 password WIFI密码
```



