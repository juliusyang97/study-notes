> 问题描述：本来是早上在学习`ros`时，遇到一个错误，于是在Ubuntu端写了一篇博客。名为`error:error-run_depend.md`,晚上在windows端再次写博客时首先需要将本地仓库更新一下，于是Git pull了一下，好家伙，出错了？？？？



```bash
 juliusyang@juliusyang F:\my_notes\study-notes
 $git pull github master
From github.com:juliusyang97/study-notes
 * branch            master     -> FETCH_HEAD
error: invalid path 'ros/error:run_depend.md'
```



草，放弃了



学习要紧，赶紧解决



找到原因了：文件命名的问题，将文件名由`error:run_depend.md`改为`error-run_depend.md`  之后pull正常了。

问题解决了，就是`：`引发的惨案