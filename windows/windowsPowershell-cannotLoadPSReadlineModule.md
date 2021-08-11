>  问题描述：前段时间搞美化powershell，结果美化没搞成（主要是系统自带的powershell版本太低，不太行，后来换了版本搞好了，文章在[这里](F:\my_notes\study-notes\blog-post\windows powershell&terminal beautify.md)），结果自带的powershell会出现一行error的东西，很是糟心，就是他

```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

Cannot load PSReadline module.  Console is running without PSReadline.
```

解决方案：

1. You will need to setup the proper Execution policy to install the required modules.
2. Import the **PowershellGet module**, this provides the ability to download modules from the[ http://www.powershellgallery.com/](http://www.powershellgallery.com/) repository.
3. Import the **PSReadLine Module**。
4. (optional) Revert your PowerShell Execution Policy.



let`s do it!!!!

**Step 1:** Setting the PowerShell [Execution Policy](https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.security/set-executionpolicy).

**Check your Powershell Execution Policy, and marked down:**

```
Get-ExecutionPolicy
```

**Run PowerShell as an Administrator and change the Execution Policy:** 

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned 
# or you can use Unrestricted
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```

**Step 2:** Import the ***PowershellGet module:***

```powershell
Execute Import-Module PowerShellGet
```

**Step 3:** Import the ***PSReadline module******:***

```powershell
Import-Module PSReadline
```

**Step 4:** (Optional, but recomended) Restore your PowerShell Execution Policy:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Restricted
```





reference:

 [How to solve the “Cannot load PSReadline module” Error when Installing the Azure CLI | Patrick Butler Monterde's Blog](https://patrickbutlermonterde.com/2017/12/20/how-to-solve-the-cannot-load-psreadline-module-error-when-installing-the-azure-cli/)