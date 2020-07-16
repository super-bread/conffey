#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/10 15:10
# 文件名称 ： Img.py
# 开发工具 ： PyCharm
import os
from PIL import Image, ImageFilter


def conver_type(img_path, new_path, new_name, flag):
    flag_list = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tif']
    img = Image.open(img_path)

    if flag == flag_list[0]:
        img=img.convert('RGB')
        img.save(os.path.join(new_path, new_name + '.jpg'), 'jpeg')
    elif flag == flag_list[1]:
        img=img.convert('RGB')
        img.save(os.path.join(new_path, new_name + '.jpeg'), 'jpeg')
    elif flag == flag_list[2]:
        img.save(os.path.join(new_path, new_name + '.png'), 'png')
    elif flag == flag_list[3]:
        img.save(os.path.join(new_path, new_name + '.gif'), 'gif')
    elif flag == flag_list[4]:
        img.save(os.path.join(new_path, new_name + '.bmp'), 'bmp')
    elif flag == flag_list[5]:
        img.save(os.path.join(new_path, new_name + '.tif'), 'tiff')


def img_resize(path, new_path, h, w):
    img = Image.open(path)
    img.resize((h, w))
    img.save(new_path)


def img_filter(path, new_path, new_name, filter_mode):
    new_img = None
    img = Image.open(path)
    mode_list = ['CONTOUR', 'BLUR', 'DETAIL', 'EDGE_ENHANCE', 'EMBOSS', 'SMOOTH', 'SHARPEN']

    if filter_mode == mode_list[0]:
        new_img = img.filter(ImageFilter.CONTOUR)
    elif filter_mode == mode_list[1]:
        new_img = img.filter(ImageFilter.BLUR)
    elif filter_mode == mode_list[2]:
        new_img = img.filter(ImageFilter.DETAIL)
    elif filter_mode == mode_list[3]:
        new_img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_mode == mode_list[4]:
        new_img = img.filter(ImageFilter.EMBOSS)
    elif filter_mode == mode_list[5]:
        new_img = img.filter(ImageFilter.SMOOTH)
    elif filter_mode == mode_list[6]:
        new_img = img.filter(ImageFilter.SHARPEN)

    new_img.save(new_path + new_name + '.png', 'png')