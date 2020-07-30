# -*- coding: utf-8 -*-
"""
@Time       :2020/7/28 16:02
@Author     :liuhuan
@verssion   :v1.0
@effect     :项目的启动文件
"""

import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.main import main
from app.auth import auth

app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.register_blueprint(main, url_prefix='/main')
app.register_blueprint(auth, url_prefix='/auth')

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    """"""
    return dict(app=app, db=db, User=User, Role=Role)

# 启动测试文件
@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover("app/tests")
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
