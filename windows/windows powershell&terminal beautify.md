# 1 安装新版powershell

## 1.1 下载安装

[在这里下载新版powershell]([PowerShell/PowerShell: PowerShell for every system! (github.com)](https://github.com/PowerShell/PowerShell))

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210519210342578.png)

windows系统下载 `xxx.msi` 文件,标准的安装文件，其他系统也是可以配置这个的

## 1.2 安装powershell插件，美化她 



1. 如果是按默认位置安装，应该合适我的路径一样。



![在这里插入图片描述](https://img-blog.csdnimg.cn/20210519210354834.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTM5MjA4MQ==,size_16,color_FFFFFF,t_70)

2. 打开刚安装好`pwsh` , 执行以下命令安装插件

```powershell
# 安装posh-git和oh-my-posh
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser


# 不想要了可以卸载
#Uninstall-Module posh-git
#Uninstall-Module oh-my-posh

```

3. 配置profile文件

```powershell
if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force
```

```powershell
notepad $PROFILE
```





这里我是参考大佬的，直接复制粘贴

```
<#
 * Search Key: powershell
 * FileName: Microsoft.PowerShell_profile.ps1
 * Author: 刘 鹏
 * Email: littleNewton6@outlook.com
 * Create Date: 2020, May. 1
 * Update Date: 2021, Apr. 7
 * Copyright: No copyright. You can use this code for anything with no warranty.
#>


#------------------------------- Import Modules BEGIN -------------------------------
# 引入 posh-git
Import-Module posh-git

# 引入 oh-my-posh
Import-Module oh-my-posh

# 引入 ps-read-line
Import-Module PSReadLine

# 设置 PowerShell 主题
# Set-PoshPrompt paradox Honukai Agnoster Avit Darkblood Fish Sorin tehrob PowerLine
Set-PoshPrompt  PowerLine

#------------------------------- Import Modules END   -------------------------------





#-------------------------------  Set Hot-keys BEGIN  -------------------------------
# 设置预测文本来源为历史记录
Set-PSReadLineOption -PredictionSource History

# 设置 Tab 为菜单补全和 Intellisense
Set-PSReadLineKeyHandler -Key "Tab" -Function MenuComplete

# 设置 Ctrl+d 为退出 PowerShell
Set-PSReadlineKeyHandler -Key "Ctrl+d" -Function ViExit

# 设置 Ctrl+z 为撤销
Set-PSReadLineKeyHandler -Key "Ctrl+z" -Function Undo

# 设置向上键为后向搜索历史记录
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward

# 设置向下键为前向搜索历史纪录
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward
#-------------------------------  Set Hot-keys END    -------------------------------





#-------------------------------    Functions BEGIN   -------------------------------
# Python 直接执行
$env:PATHEXT += ";.py"

# 更新系统组件
function Update-Packages {
	# update pip
	Write-Host "Step 1: 更新 pip" -ForegroundColor Magenta -BackgroundColor Cyan
	$a = pip list --outdated
	$num_package = $a.Length - 2
	for ($i = 0; $i -lt $num_package; $i++) {
		$tmp = ($a[2 + $i].Split(" "))[0]
		pip install -U $tmp
	}

	# update TeX Live
	$CurrentYear = Get-Date -Format yyyy
	Write-Host "Step 2: 更新 TeX Live" $CurrentYear -ForegroundColor Magenta -BackgroundColor Cyan
	tlmgr update --self
	tlmgr update --all

	# update Chocolotey
	Write-Host "Step 3: 更新 Chocolatey" -ForegroundColor Magenta -BackgroundColor Cyan
	choco outdated
}
#-------------------------------    Functions END     -------------------------------





#-------------------------------   Set Alias BEGIN    -------------------------------
# 1. 编译函数 make
function MakeThings {
	nmake.exe $args -nologo
}
Set-Alias -Name make -Value MakeThings

# 2. 更新系统 os-update
Set-Alias -Name os-update -Value Update-Packages

# 3. 查看目录 ls & ll
function ListDirectory {
	(Get-ChildItem).Name
	Write-Host("")
}
Set-Alias -Name ls -Value ListDirectory
Set-Alias -Name ll -Value Get-ChildItem

# 4. 打开当前工作目录
function OpenCurrentFolder {
	Invoke-Item .
}
Set-Alias -Name open -Value OpenCurrentFolder
#-------------------------------    Set Alias END     -------------------------------
```

------

----

啊，不想写了，先放几个链接，以后写不写再说吧！！！



windows terminal下载地址:

[Get Windows Terminal - Microsoft Store]([Get Windows Terminal - Microsoft Store](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab))

[github-repo]([Release Windows Terminal v1.7.1091.0 (Scoop Compatibility) · microsoft/terminal (github.com)](https://github.com/microsoft/terminal/releases/tag/v1.7.1091.0))



windows terminal config :

settings.json 文件内容如下

```json
{
    "$schema": "https://aka.ms/terminal-profiles-schema",
    "alwaysShowTabs": true,
    "confirmCloseAllTabs": false,
    "defaultProfile": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
    // 禁止自动生成
    "disabledProfileSources": 
    [
        "Windows.Terminal.Azure"
    ],
    "initialCols": 82,
    "initialPosition": "320,65",
    "initialRows": 22,
    // ======================== COLOR SCHEME 配置 END   ========================
    // ======================== HOTKEY 配置 BEGIN ========================
    "keybindings": 
    [
        // ======================== 1. 界面视图 配置 BEGIN ========================
        // 1.1 调节字体大小
        {
            "command": 
            {
                "action": "adjustFontSize",
                "delta": 1
            },
            "keys": "ctrl+="
        },
        {
            "command": 
            {
                "action": "adjustFontSize",
                "delta": -1
            },
            "keys": "ctrl+-"
        },
        {
            "command": "resetFontSize",
            "keys": "ctrl+0"
        },
        // ======================== 1. 界面视图 配置 END   ========================
        // ======================== 2. PANE 分割 配置 BEGIN ========================
        // 2.1 水平、竖直分割
        {
            "command": 
            {
                "action": "splitPane",
                "split": "horizontal"
            },
            "keys": "alt+shift+-"
        },
        {
            "command": 
            {
                "action": "splitPane",
                "split": "vertical"
            },
            "keys": "alt+shift+plus"
        },
        {
            "command": 
            {
                "action": "splitPane",
                "split": "auto"
            },
            "keys": "alt+shift+|"
        },
        {
            "command": 
            {
                "action": "splitPane",
                "split": "auto",
                "splitMode": "duplicate"
            },
            "keys": "alt+shift+d"
        },
        {
            "command": 
            {
                "action": "splitPane",
                "profile": "Ubuntu-20.04",
                "split": "horizontal"
            },
            "keys": "alt+shift+u"
        },
        // 2.2 按下 Alt 键，同时按下方向键，在多个 pane 之间切换
        {
            "command": 
            {
                "action": "moveFocus",
                "direction": "down"
            },
            "keys": "alt+down"
        },
        {
            "command": 
            {
                "action": "moveFocus",
                "direction": "left"
            },
            "keys": "alt+left"
        },
        {
            "command": 
            {
                "action": "moveFocus",
                "direction": "right"
            },
            "keys": "alt+right"
        },
        {
            "command": 
            {
                "action": "moveFocus",
                "direction": "up"
            },
            "keys": "alt+up"
        },
        // 2.3 按下 Alt + Shift，同时按下方向键，调整当前 pane 的大小
        {
            "command": 
            {
                "action": "resizePane",
                "direction": "down"
            },
            "keys": "alt+shift+down"
        },
        {
            "command": 
            {
                "action": "resizePane",
                "direction": "left"
            },
            "keys": "alt+shift+left"
        },
        {
            "command": 
            {
                "action": "resizePane",
                "direction": "right"
            },
            "keys": "alt+shift+right"
        },
        {
            "command": 
            {
                "action": "resizePane",
                "direction": "up"
            },
            "keys": "alt+shift+up"
        },
        // 2.4 关闭 pane
        {
            "command": "closePane",
            "keys": "alt+shift+w"
        },
        // ======================== 2. PANE 分割 配置 BEGIN ========================
        // ======================== 3. 关于标签 配置 BEGIN ========================
        // 3.1 新建默认标签页
        {
            "command": "newTab",
            "keys": 
            [
                "ctrl+n"
            ]
        },
        // 3.2 新建 N 号 profile 的标签
        {
            "command": 
            {
                "action": "newTab",
                "index": 0
            },
            "keys": "ctrl+shift+1"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 1
            },
            "keys": "ctrl+shift+2"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 2
            },
            "keys": "ctrl+shift+3"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 3
            },
            "keys": "ctrl+shift+4"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 4
            },
            "keys": "ctrl+shift+5"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 5
            },
            "keys": "ctrl+shift+6"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 6
            },
            "keys": "ctrl+shift+7"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 7
            },
            "keys": "ctrl+shift+8"
        },
        {
            "command": 
            {
                "action": "newTab",
                "index": 8
            },
            "keys": "ctrl+shift+9"
        },
        // 3.3 切换到第 N 个标签页
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 0
            },
            "keys": "ctrl+alt+1"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 1
            },
            "keys": "ctrl+alt+2"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 2
            },
            "keys": "ctrl+alt+3"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 3
            },
            "keys": "ctrl+alt+4"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 4
            },
            "keys": "ctrl+alt+5"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 5
            },
            "keys": "ctrl+alt+6"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 6
            },
            "keys": "ctrl+alt+7"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 7
            },
            "keys": "ctrl+alt+8"
        },
        {
            "command": 
            {
                "action": "switchToTab",
                "index": 8
            },
            "keys": "ctrl+alt+9"
        },
        // 3.4 -> <- 标签页间切换
        {
            "command": "nextTab",
            "keys": "ctrl+tab"
        },
        {
            "command": "prevTab",
            "keys": "ctrl+shift+tab"
        },
        {
            "command": "duplicateTab",
            "keys": "ctrl+shift+d"
        },
        // 3.5 关闭标签页
        {
            "command": "closeTab",
            "keys": "ctrl+w"
        },
        // ======================== 3. 关于标签 配置 END   ========================
        // ======================== 4. 杂项热键 配置 BEGIN ========================
        // 4.1 搜索
        {
            "command": "find",
            "keys": "ctrl+f"
        },
        // 4.2 打开 settings.json 
        {
            "command": "openSettings",
            "keys": "ctrl+;"
        },
        // 4.3 复制、粘贴
        {
            "command": 
            {
                "action": "copy",
                "singleLine": false
            },
            "keys": "ctrl+shift+c"
        },
        {
            "command": 
            {
                "action": "copy",
                "singleLine": false
            },
            "keys": "ctrl+insert"
        },
        {
            "command": "paste",
            "keys": "ctrl+shift+v"
        },
        {
            "command": "paste",
            "keys": "shift+insert"
        },
        // 4.4 上下滚动、上下整页滚动
        {
            "command": "scrollDown",
            "keys": "ctrl+shift+down"
        },
        {
            "command": "scrollUp",
            "keys": "ctrl+shift+up"
        },
        {
            "command": "scrollDownPage",
            "keys": "ctrl+shift+pgdn"
        },
        {
            "command": "scrollUpPage",
            "keys": "ctrl+shift+pgup"
        }
    ],
    "launchMode": "default",
    "profiles": 
    {
        "defaults": {},
        "list": 
        [
            {
                "acrylicOpacity": 0.5,
                "backgroundImage": null,
                "backgroundImageOpacity": 1.0,
                "backgroundImageStretchMode": "uniformToFill",
                "closeOnExit": "graceful",
                "colorScheme": "Campbell Powershell",
                "commandline": "C:/Program Files/PowerShell/7/pwsh.exe -nologo",
                "cursorColor": "#FFFFFF",
                "cursorShape": "bar",
                "fontFace": "MesloLGM NF",
                "fontSize": 11,
                "guid": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
                "hidden": false,
                "historySize": 9001,
                "icon": "C:\\Program Files\\PowerShell\\7\\assets\\Powershell_av_colors.ico",
                "name": "PowerShell Core 7.1.3",
                "padding": "10",
                "snapOnInput": true,
                "source": "Windows.Terminal.PowershellCore",
                "startingDirectory": ".",
                "useAcrylic": true
            },
            {
                "commandline": "cmd.exe",
                "fontFace": "Fira Code",
                "fontSize": 11,
                "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
                "hidden": false,
                "name": "cmd"
            },
            {
                "acrylicOpacity": 0.5,
                "closeOnExit": "graceful",
                "colorScheme": "Homebrew",
                "commandline": "powershell.exe",
                "cursorColor": "#FFFFFF",
                "cursorShape": "bar",
                "fontFace": "Fira Code",
                "fontSize": 11,
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "hidden": true,
                "historySize": 9001,
                "name": "Windows PowerShell",
                "padding": "5, 5, 20, 25",
                "snapOnInput": true,
                "startingDirectory": ".",
                "useAcrylic": false
            },
            {
                "acrylicOpacity": 0.75,
                "colorScheme": "Homebrew",
                "commandline": "E:\\Git\\git-bash.exe",
                "fontFace": "Fira Code",
                "hidden": false,
                "icon": "E:\\Git\\mingw64\\share\\git\\git-for-windows.ico",
                "name": "git bash",
                "tabTitle": "Git",
                "useAcrylic": true
            }
        ]
    },
    "schemes": 
    [
        {
            "background": "#0C0C0C",
            "black": "#0C0C0C",
            "blue": "#0037DA",
            "brightBlack": "#767676",
            "brightBlue": "#3B78FF",
            "brightCyan": "#61D6D6",
            "brightGreen": "#16C60C",
            "brightPurple": "#B4009E",
            "brightRed": "#E74856",
            "brightWhite": "#F2F2F2",
            "brightYellow": "#F9F1A5",
            "cursorColor": "#FFFFFF",
            "cyan": "#3A96DD",
            "foreground": "#CCCCCC",
            "green": "#13A10E",
            "name": "Campbell",
            "purple": "#881798",
            "red": "#C50F1F",
            "selectionBackground": "#FFFFFF",
            "white": "#CCCCCC",
            "yellow": "#C19C00"
        },
        {
            "background": "#012456",
            "black": "#0C0C0C",
            "blue": "#0037DA",
            "brightBlack": "#767676",
            "brightBlue": "#3B78FF",
            "brightCyan": "#61D6D6",
            "brightGreen": "#16C60C",
            "brightPurple": "#B4009E",
            "brightRed": "#E74856",
            "brightWhite": "#F2F2F2",
            "brightYellow": "#F9F1A5",
            "cursorColor": "#FFFFFF",
            "cyan": "#3A96DD",
            "foreground": "#CCCCCC",
            "green": "#13A10E",
            "name": "Campbell Powershell",
            "purple": "#881798",
            "red": "#C50F1F",
            "selectionBackground": "#FFFFFF",
            "white": "#CCCCCC",
            "yellow": "#C19C00"
        },
        {
            "background": "#283033",
            "black": "#000000",
            "blue": "#6666E9",
            "brightBlack": "#666666",
            "brightBlue": "#00A2FF",
            "brightCyan": "#53FFFF",
            "brightGreen": "#00D900",
            "brightPurple": "#FF08FF",
            "brightRed": "#FF6060",
            "brightWhite": "#E5E5E5",
            "brightYellow": "#FDFF73",
            "cursorColor": "#FFFFFF",
            "cyan": "#00A6B2",
            "foreground": "#00FF00",
            "green": "#00A600",
            "name": "Homebrew",
            "purple": "#FF00FF",
            "red": "#FC5275",
            "selectionBackground": "#FFFFFF",
            "white": "#BFBFBF",
            "yellow": "#FFFF00"
        },
        {
            "background": "#282C34",
            "black": "#282C34",
            "blue": "#61AFEF",
            "brightBlack": "#5A6374",
            "brightBlue": "#61AFEF",
            "brightCyan": "#56B6C2",
            "brightGreen": "#98C379",
            "brightPurple": "#C678DD",
            "brightRed": "#E06C75",
            "brightWhite": "#DCDFE4",
            "brightYellow": "#E5C07B",
            "cursorColor": "#FFFFFF",
            "cyan": "#56B6C2",
            "foreground": "#DCDFE4",
            "green": "#98C379",
            "name": "One Half Dark",
            "purple": "#C678DD",
            "red": "#E06C75",
            "selectionBackground": "#FFFFFF",
            "white": "#DCDFE4",
            "yellow": "#E5C07B"
        },
        {
            "background": "#FAFAFA",
            "black": "#383A42",
            "blue": "#0184BC",
            "brightBlack": "#4F525D",
            "brightBlue": "#61AFEF",
            "brightCyan": "#56B5C1",
            "brightGreen": "#98C379",
            "brightPurple": "#C577DD",
            "brightRed": "#DF6C75",
            "brightWhite": "#FFFFFF",
            "brightYellow": "#E4C07A",
            "cursorColor": "#4F525D",
            "cyan": "#0997B3",
            "foreground": "#383A42",
            "green": "#50A14F",
            "name": "One Half Light",
            "purple": "#A626A4",
            "red": "#E45649",
            "selectionBackground": "#FFFFFF",
            "white": "#FAFAFA",
            "yellow": "#C18301"
        },
        {
            "background": "#002B36",
            "black": "#002B36",
            "blue": "#268BD2",
            "brightBlack": "#073642",
            "brightBlue": "#839496",
            "brightCyan": "#93A1A1",
            "brightGreen": "#586E75",
            "brightPurple": "#6C71C4",
            "brightRed": "#CB4B16",
            "brightWhite": "#FDF6E3",
            "brightYellow": "#657B83",
            "cursorColor": "#FFFFFF",
            "cyan": "#2AA198",
            "foreground": "#839496",
            "green": "#859900",
            "name": "Solarized Dark",
            "purple": "#D33682",
            "red": "#DC322F",
            "selectionBackground": "#FFFFFF",
            "white": "#EEE8D5",
            "yellow": "#B58900"
        },
        {
            "background": "#FDF6E3",
            "black": "#002B36",
            "blue": "#268BD2",
            "brightBlack": "#073642",
            "brightBlue": "#839496",
            "brightCyan": "#93A1A1",
            "brightGreen": "#586E75",
            "brightPurple": "#6C71C4",
            "brightRed": "#CB4B16",
            "brightWhite": "#FDF6E3",
            "brightYellow": "#657B83",
            "cursorColor": "#002B36",
            "cyan": "#2AA198",
            "foreground": "#657B83",
            "green": "#859900",
            "name": "Solarized Light",
            "purple": "#D33682",
            "red": "#DC322F",
            "selectionBackground": "#FFFFFF",
            "white": "#EEE8D5",
            "yellow": "#B58900"
        },
        {
            "background": "#000000",
            "black": "#000000",
            "blue": "#3465A4",
            "brightBlack": "#555753",
            "brightBlue": "#729FCF",
            "brightCyan": "#34E2E2",
            "brightGreen": "#8AE234",
            "brightPurple": "#AD7FA8",
            "brightRed": "#EF2929",
            "brightWhite": "#EEEEEC",
            "brightYellow": "#FCE94F",
            "cursorColor": "#FFFFFF",
            "cyan": "#06989A",
            "foreground": "#D3D7CF",
            "green": "#4E9A06",
            "name": "Tango Dark",
            "purple": "#75507B",
            "red": "#CC0000",
            "selectionBackground": "#FFFFFF",
            "white": "#D3D7CF",
            "yellow": "#C4A000"
        },
        {
            "background": "#FFFFFF",
            "black": "#000000",
            "blue": "#3465A4",
            "brightBlack": "#555753",
            "brightBlue": "#729FCF",
            "brightCyan": "#34E2E2",
            "brightGreen": "#8AE234",
            "brightPurple": "#AD7FA8",
            "brightRed": "#EF2929",
            "brightWhite": "#EEEEEC",
            "brightYellow": "#FCE94F",
            "cursorColor": "#000000",
            "cyan": "#06989A",
            "foreground": "#555753",
            "green": "#4E9A06",
            "name": "Tango Light",
            "purple": "#75507B",
            "red": "#CC0000",
            "selectionBackground": "#FFFFFF",
            "white": "#D3D7CF",
            "yellow": "#C4A000"
        },
        {
            "background": "#000000",
            "black": "#000000",
            "blue": "#000080",
            "brightBlack": "#808080",
            "brightBlue": "#0000FF",
            "brightCyan": "#00FFFF",
            "brightGreen": "#00FF00",
            "brightPurple": "#FF00FF",
            "brightRed": "#FF0000",
            "brightWhite": "#FFFFFF",
            "brightYellow": "#FFFF00",
            "cursorColor": "#FFFFFF",
            "cyan": "#008080",
            "foreground": "#C0C0C0",
            "green": "#008000",
            "name": "Vintage",
            "purple": "#800080",
            "red": "#800000",
            "selectionBackground": "#FFFFFF",
            "white": "#C0C0C0",
            "yellow": "#808000"
        }
    ],
    "tabSwitcherMode": "mru",
    "tabWidthMode": "equal",
    "theme": "system"
}
```





powerline 主题提示符为乱码或是方框解决：安装以下字体

windows terminal powerline fonts：[Meslo LGM NF](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Meslo.zip)