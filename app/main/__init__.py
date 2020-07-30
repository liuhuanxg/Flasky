# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:01
@Author     :liuhuan
@verssion   :v1.0
@effect     :初始化蓝图
"""

from flask import Blueprint

main = Blueprint("main", __name__)

from . import views, errors
