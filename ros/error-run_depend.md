> 在执行ros官方教程
```
rosmsg show beginner_tutorials/Num
```
报错如下：
```
Traceback (most recent call last):
  File "/opt/ros/kinetic/bin/rosmsg", line 35, in <module>
    rosmsg.rosmsgmain()
  File "/opt/ros/kinetic/lib/python2.7/dist-packages/rosmsg/__init__.py", line 754, in rosmsgmain
    sys.exit(rosmsg_cmd_show(ext, full, command))
  File "/opt/ros/kinetic/lib/python2.7/dist-packages/rosmsg/__init__.py", line 619, in rosmsg_cmd_show
    rosmsg_debug(rospack, mode, arg, options.raw)
  File "/opt/ros/kinetic/lib/python2.7/dist-packages/rosmsg/__init__.py", line 450, in rosmsg_debug
    print(get_msg_text(type_, raw=raw, rospack=rospack))
  File "/opt/ros/kinetic/lib/python2.7/dist-packages/rosmsg/__init__.py", line 427, in get_msg_text
    package_paths = _get_package_paths(p, rospack)
  File "/opt/ros/kinetic/lib/python2.7/dist-packages/rosmsg/__init__.py", line 554, in _get_package_paths
    results = find_in_workspaces(search_dirs=['share'], project=pkgname, first_match_only=True, workspace_to_source_spaces=_catkin_workspace_to_source_spaces, source_path_to_packages=_catkin_source_path_to_packages)
  File "/opt/ros/kinetic/lib/python2.7/dist-packages/catkin/find_in_workspaces.py", line 149, in find_in_workspaces
    source_path_to_packages[source_path] = find_packages(source_path)
  File "/usr/lib/python2.7/dist-packages/catkin_pkg/packages.py", line 87, in find_packages
    packages = find_packages_allowing_duplicates(basepath, exclude_paths=exclude_paths, exclude_subspaces=exclude_subspaces, warnings=warnings)
  File "/usr/lib/python2.7/dist-packages/catkin_pkg/packages.py", line 148, in find_packages_allowing_duplicates
    xml, filename=filename, warnings=warnings)
  File "/usr/lib/python2.7/dist-packages/catkin_pkg/package.py", line 771, in parse_package_string
    raise InvalidPackage('Error(s):%s' % (''.join(['\n- %s' % e for e in errors])), filename)
catkin_pkg.package.InvalidPackage: Error(s) in package '/home/julius/catkin_ws_1/src/beginner_tutorials/package.xml':
Error(s):
- The manifest of package "beginner_tutorials" (with format version 2) must not contain the following tags: run_depend
- Please replace <run_depend> tags with <exec_depend> tags.
```

解决方案：

**睁大眼睛看报错信息最后一行，使用新版的依赖标签**





