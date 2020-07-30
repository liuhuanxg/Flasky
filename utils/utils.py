# -*- coding: utf-8 -*-
"""
@Time       :2020/7/30 16:37
@Author     :liuhuan
@verssion   :v1.0
@effect     :工具包
"""

import hashlib
#加密
def set_md5(value):
    md = hashlib.md5()
    md.update(value.encode('utf-8'))
    md5_value = md.hexdigest()
    return md5_value

def set_pwd(value):
    return set_md5(set_md5(set_md5(value)))
