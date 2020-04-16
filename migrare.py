#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : migrare.py
# @Time : 2020/3/9 2:16 PM


from api import create_app
from api.models import db

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
