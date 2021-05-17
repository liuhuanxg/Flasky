from flask import url_for, redirect
from app.auth.views import session, request
from functools import wraps


# 校验用户是否登录
def login_valid(func):
    @wraps(func)
    def inner():
        if session.get("user_username", "") and session.get("user_id", ""):
            print(session)
            return func()
        return redirect(url_for("auth.login"))

    return inner()
