# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:03
@Author     :liuhuan
@verssion   :v1.0
@effect     :数据库模型文件
"""

from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# 用户角色类
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name


# 用户表
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    password_hash =  db.Column(db.String(128))

    @property
    def password(self):
        raise ArithmeticError("password is not readable attribute")

    @password.setter
    def password(self,password):
        self.password_hash =  generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User %r>" % self.username
