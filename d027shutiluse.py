#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author : Lmc  Date: 17-9-8 下午4:43


# shutil 高级的文件、文件夹、压缩包处理模块
import shutil

# 复制方法1：
# with open('d014file', 'r') as f, open('d027copyfile', 'w') as f1:
# 	shutil.copyfileobj(f, f1)

# 复制方法2：
# shutil.copyfile('d014file', 'd027copyfile')

# 仅拷贝权限。内容、组、用户均不变
# shutil.copymode('d014file', 'd027copyfile')

# 拷贝状态的信息，包括：mode bits，atime， mtime，flags
# shutil.copystat('d014file', 'd027copyfile')

# 拷贝文件和权限
# shutil.copy('d014file', 'd027copyfile')

# 拷贝文件和状态信息
# shutil.copy2('d014file', 'd027copyfile')

# 复制文件目录及其文件
# shutil.copytree('filedirectory1', 'filedirectory2')
# 删除文件目录及其文件
# shutil.rmtree('filedirectory2')

# shutil.make_archive('www','gztar','root_dir',)
# 创建压缩包并返回文件路径，例如：zip、tar
#
#     base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
#     如：www                        =>保存至当前路径
#     如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
#     format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
#     root_dir： 要压缩的文件夹路径（默认当前目录）
#     owner： 用户，默认当前用户
#     group： 组，默认当前组
#     logger： 用于记录日志，通常是logging.Logger对象
