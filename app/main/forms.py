# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:02
@Author     :liuhuan
@verssion   :v1.0
@effect     :定义表单类
"""
from flask_wtf import Form  # 引入表单
from wtforms import StringField, SubmitField  # 引入表单字段类型
from wtforms.validators import Required  # 引入数据校验的必填属性


# 定义用户登录类
class NameForm(Form):
    name = StringField("姓名：", validators=[Required()])
    submit = SubmitField("提交")
