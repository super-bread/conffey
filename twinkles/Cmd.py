#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： Czf陈章辅
# 开发人员 ： 陈章辅(Administrator)
# 开发时间 ： 2020/7/5 15:53
# 文件名称 ： Cmd.py
# 开发工具 ： PyCharm
import math
import sys
import time
import hashlib
import hmac
from xpinyin import Pinyin


# DONE
def clock_list():
    now = time.strftime
    clk = [now('%Y-%m-%d'), now('%H:%M:%S'), now('%p'), now('%I'), now('%A'), now('%j'), now('%U')]
    return clk


# DONE
def clock_str():
    now = time.strftime('%Y-%m-%d  %H:%M:%S')
    return now


# DONE
def inv_str(s):
    rtn = ''.join(s[::-1])
    return rtn


# DONE
def inv_list(s):
    rtn = s[::-1]
    return rtn


# DONE
def inv_num(n):
    tmp1 = str(n)
    tmp2 = ''.join(tmp1[::-1])
    rtn = float(tmp2)
    return rtn


# DONE
def load_a(trns):
    i = 0
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write('请稍等,精彩马上呈现... ')

    for foo in range(trns):
        sys.stdout.write('—')

        time.sleep(0.25)
        sys.stdout.write('\b')
        sys.stdout.write('\\')

        time.sleep(0.25)
        sys.stdout.write('\b')
        sys.stdout.write('|')

        time.sleep(0.25)
        sys.stdout.write('\b')
        sys.stdout.write('/')

        time.sleep(0.25)
        sys.stdout.write('\b')


# DONE
def load_b(trns):
    sys.stdout.write('\r')
    sys.stdout.flush()

    for foo in range(trns):
        sys.stdout.write('请稍等,精彩马上呈现')
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write(' ')
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('\r')


# DONE
def get_location_code(words, sep=' '):
    tmp = []

    for w in words:
        gbk = w.encode('gbk')
        code = '{0:02d}'.format((gbk[0] - 160)) + '{0:02d}'.format((gbk[1] - 160))
        tmp.append(code)

    rtn = sep.join(tmp)
    return rtn


# DONE
def draw_par(speed, angle, miles, par_char='O'):
    """
    draw_par
    :param speed: 速度
    :param angle: 角度
    :param miles: 英里
    :param par_char: 描述抛物线的字符 (默认为 O (字母O))
    :return: None
    """

    for x in range(miles + 1):
        print('%04d' % x,
              ' ' * math.floor(0.5 + x * math.tan(speed) - x * x / (angle * math.cos(speed))) + par_char,
              sep='')


# DONE
def check_ver(ver=3):
    __MAJOR, __MINOR, __MICRO = sys.version_info[0], sys.version_info[1], sys.version_info[2]
    if __MAJOR != ver:
        print('Python版本与本程序不兼容, 当前版本为 %d.%d.%d' % (__MAJOR, __MINOR, __MICRO))
        exit()


# DONE
def sort_chinese_list(words, reverse=False):
    pinyin = Pinyin()

    temp = []
    for item in words:
        temp.append((pinyin.get_pinyin(item), item))
    temp.sort(reverse=reverse)

    rtn = []
    for i in range(len(temp)):
        rtn.append(temp[i][1])
    return rtn


# DONE
def sort_chinese_str(words, reverse=False, sep=' '):
    pinyin = Pinyin()

    temp = []
    for item in words:
        temp.append((pinyin.get_pinyin(item), item))
    temp.sort(reverse=reverse)

    rtn = []
    for i in range(len(temp)):
        rtn.append(temp[i][1])
    rtn = sep.join(rtn)
    return rtn


# DONE
def get_pinyin(words, sep=' '):
    pinyin = Pinyin()
    rtn = pinyin.get_pinyin(words, splitter=sep)
    return rtn


# DONE
def encryption(string, lib='md5', is_hmac=True, encoding='utf-8'):
    libs = ['md5', 'sha1', 'sha256', 'sha512']
    if is_hmac:
        if not lib in libs:
            raise ValueError('无此模式')
        else:
            if lib == libs[0]:
                s = string.encode(encoding)
                key = 'ki'.encode(encoding)
                h = hmac.new(key, s, digestmod='MD5')
                return h.hexdigest()

            if lib == libs[1]:
                s = string.encode(encoding)
                key = 'kz'.encode(encoding)
                h = hmac.new(key, s, digestmod='SHA1')
                return h.hexdigest()

            if lib == libs[2]:
                s = string.encode(encoding)
                key = 'ke'.encode(encoding)
                h = hmac.new(key, s, digestmod='SHA256')
                return h.hexdigest()

            if lib == libs[3]:
                s = string.encode(encoding)
                key = 'kq'.encode(encoding)
                h = hmac.new(key, s, digestmod='SHA512')
                return h.hexdigest()
    else:
        if not lib in libs:
            raise ValueError('无此模式')
        else:
            if lib == libs[0]:
                md5 = hashlib.md5()
                md5.update(string.encode(encoding))
                return md5.hexdigest()

            if lib == libs[1]:
                sha1 = hashlib.sha1()
                sha1.update(string.encode(encoding))
                return sha1.hexdigest()

            if lib == libs[2]:
                sha256 = hashlib.sha256()
                sha256.update(string.encode(encoding))
                return sha256.hexdigest()

            if lib == libs[3]:
                sha512 = hashlib.sha512()
                sha512.update(string.encode(encoding))
                return sha512.hexdigest()
