#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : test_course_type.py
# @Time : 2020/3/9 2:41 PM

import unittest

from api import create_app
from api.models import db
from api.models.home import CourseTypeModel


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

    def test_course_type(self):
        course_type = CourseTypeModel(course_type='Flink')
        db.session.add(course_type)
        db.session.commit()
