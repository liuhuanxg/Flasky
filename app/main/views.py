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
    return render_template("base/blank.html")

@main.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", current_time=datetime.utcnow())
