#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/5 15:54
# 文件名称 ： File.py
# 开发工具 ： PyCharm
import os


# DONE
def create_file(file_path):
    f = open(file_path, 'w+')
    f.close()


# DONE
def delete_file(path, is_all=False):
    if not is_all:
        os.remove(path)
    elif is_all:
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(os.path.join(root, file))


# DONE
def read_file(file_path, size=0, mode='r', coding='utf-8'):
    if size != 0:
        if os.path.exists(file_path):
            with open(file_path, mode=mode, encoding=coding) as f:
                rtn = f.read(size)
        else:
            rtn = 0
        return rtn
    else:
        if os.path.exists(file_path):
            with open(file_path, mode=mode, encoding=coding) as f:
                rtn = f.read()
        else:
            rtn = 0
        return rtn


# DONE
def write_file(file_path, content, mode='w', coding='utf-8'):
    with open(file_path, mode=mode, encoding=coding) as f:
        f.write(content)
