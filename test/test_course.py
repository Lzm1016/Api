#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : test_course.py
# @Time : 2020/3/9 3:12 PM
from datetime import datetime

import pandas as pd

import unittest

from api import create_app
from api.comm.utils import uuid_str
from api.models import db
from api.models.home import CourseModel


class ModelTest(unittest.TestCase):
    def setUp(self):
        # 开始 准备
        self.app = create_app()
        self.app_ctx = self.app.app_context()
        # 推进app
        self.app_ctx.push()
        # db.drop_all()
        # db.create_all()

    def tearDown(self):
        # 结束 清理
        self.app_ctx.pop()

    def test_user_role_set(self):

        courses = CourseModel.query.all()
        all = []
        for cou in courses:
            cou.update_time = datetime.now()
            all.append(cou)
        db.session.add_all(all)
        db.session.commit()
