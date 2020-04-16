#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : __init__.py.py
# @Time : 2020/3/6 5:03 PM

from flask import Flask
from config import config


def create_app(conf='default'):
    from . import models, routes

    app = Flask(__name__)
    app.config.from_object(config[conf])

    models.init_app(app)
    routes.init(app)

    return app
