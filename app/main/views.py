# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:02
@Author     :liuhuan
@verssion   :v1.0
@effect     :处理业务逻辑
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route("/base")
def base():
    return render_template("base/base.html")

@main.route("/", methods=["GET", "POST"])
def index():
    Form = NameForm()
    if Form.validate_on_submit():
        username = Form.name.data
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
        session["name"] = user.username
        Form.name.data = ""
        # 使用重定向可以再刷新页面时不提示是否提交表单数据
        return redirect(url_for("mian.index"))
    return render_template("index.html", form=Form, name=session.get("name"), known=session.get("known", False), current_time=datetime.utcnow())
