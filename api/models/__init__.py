#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : __init__.py.py
# @Time : 2020/3/6 6:28 PM


from .base import db


def init_app(app):
    db.init_app(app)
