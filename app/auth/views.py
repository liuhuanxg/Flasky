# -*- coding: utf-8 -*-
"""
@Time       :2020/7/30 13:28
@Author     :liuhuan
@verssion   :v1.0
@effect     :业务逻辑处理
"""
from flask import render_template, request, redirect, url_for
from . import auth
from .. import db
from ..models import User, Role


# 登录
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form
        username = data.get("username", "")
        email = data.get("email", "")
        pwd = data.get("pwd", "")
        pwd_confirm = data.get("pwd_confirm", "")

        print(data, 111111)
        return redirect(url_for("main"))
    return render_template("auth/login.html")


# 注册
@auth.route("/register", methods=["GET", "POST"])
def register():
    error = request.args.get("error", "")
    print("error", error)
    if request.method == "POST":
        data = request.form
        username = data.get("username", "")
        email = data.get("email", "")
        pwd = data.get("pwd", "")
        pwd_confirm = data.get("pwd_confirm", "")
        agreeterms = data.get("agreeterms", "")
        user = User.query.filter_by(username=username).first()
        user_email = User.query.filter_by(username=username).first()
        if agreeterms and not user and pwd_confirm == pwd and not user_email:
            u = User(username=username, email=email, password_hash=pwd)
            u.save()
            return redirect(url_for("auth.login"))
        else:
            if not agreeterms:
                error += "请勾选同意协议。"
            if user:
                error += "用户名重复。"
            if pwd != pwd_confirm:
                error += "两次密码不一致。"
            if user_email:
                error += "邮箱重复。"
            return redirect(url_for("auth.register", error=error))
    return render_template("auth/register.html", error=error)
