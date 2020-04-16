#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : __init__.py.py
# @Time : 2020/3/6 5:03 PM

from .home import home_bp


def init(app):
    app.register_blueprint(home_bp, url_prefix='/api')
