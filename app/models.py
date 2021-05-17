# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:03
@Author     :liuhuan
@verssion   :v1.0
@effect     :数据库模型文件
"""

from . import db
from utils.utils import set_pwd
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


# 用户角色类
class Role(BaseModel):
    __tablename__ = "roles"

    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name


# 用户表
class User(BaseModel):
    __tablename__ = "users"

    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(32), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    password_hash = db.Column(db.String(128))

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = set_pwd(password_hash)

    @property
    def password(self):
        raise ArithmeticError("password is not readable attribute")

    def __repr__(self):
        return "<User %r>" % self.username
