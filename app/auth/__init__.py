# -*- coding: utf-8 -*-
"""
@Time       :2020/7/30 13:27
@Author     :liuhuan
@verssion   :v1.0
@effect     :用户身份认证相关
"""
from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views
