# -*- coding: utf-8 -*-
"""
@Time       :2020/7/30 13:28
@Author     :liuhuan
@verssion   :v1.0
@effect     :业务逻辑处理
"""
from flask import render_template
from . import auth


# 登录
@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("auth/login.html")


# 注册
@auth.route("/register", methods=["GET", "POST"])
def register():
    return render_template("auth/register.html")
