# -*- coding: utf-8 -*-
"""
@Time       :2020/7/30 13:28
@Author     :liuhuan
@verssion   :v1.0
@effect     :业务逻辑处理
"""
from flask import render_template, request, redirect, url_for, session
from . import auth
from app import db
from ..models import User, Role
from utils.utils import set_pwd


# 登录
@auth.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    try:
        if request.method == "POST":
            data = request.form
            username = data.get("username", "")
            email = data.get("email", "")
            pwd = data.get("pwd", "")
            print(username, set_pwd(pwd))
            user = User.query.filter_by(username=username, password_hash=set_pwd(pwd)).first()
            e_user = User.query.filter_by(email=email, password_hash=set_pwd(pwd)).first()
            if user or e_user:
                session["user_username"] = user.username
                session["user_id"] = user.id
                print(session.get("user_id"))
                return redirect(url_for("main.index"))
            error = "账号或密码有误"
    except Exception as E:
        print("【login error】", E)
    return render_template("auth/login.html", error=error)


# 注册
@auth.route("/register", methods=["GET", "POST"])
def register():
    error = request.args.get("error", "")
    print("error", error)
    try:
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
    except Exception as E:
        print("【register error】", E)
    return render_template("auth/register.html", error=error)


@auth.route("/logout")
def logout():
    try:
        del session["user_username"]
        del session["user_id"]
    except Exception as E:
        print("【logout】:", E)
    return redirect(url_for("auth.login"))
