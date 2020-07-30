# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:02
@Author     :liuhuan
@verssion   :v1.0
@effect     :蓝图中的错误处理程序
"""

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"),404

@main.app_errorhandler(500)
def page_not_found(e):
    return render_template("error/500.html"),500