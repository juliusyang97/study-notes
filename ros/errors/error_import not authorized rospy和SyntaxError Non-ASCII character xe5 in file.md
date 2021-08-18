记录一下遇到的错误：

1. 如果Python文件中有中文，会抛出异常`SyntaxError: Non-ASCII character '\xe5' in file`

​    

​    解决方法：在Python文件前加上一句

```python
#coding=utf-8
```

2. 在运行python时，抛出异常`import: not authorized `rospy' @ error/constitute.c/WriteImage/1028.`



​    解决方法：在python文件前面加上一句  --> 指定一下解释器

```python
#! /usr/bin/env python
```

3. 如果吧`#coding=utf-8`放在第一行，`#! /usr/bin/env python`放在第二行，还是会出现问题2，所以他们之间的顺序应该如下：

    ```python
    #! /usr/bin/env python
    #coding=utf-8
    ```



