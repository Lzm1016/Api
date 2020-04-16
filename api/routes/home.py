#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : home.py
# @Time : 2020/3/6 5:03 PM

from flask import Blueprint
from flask_restful import Api

from api.comm.errcode_enum import ErrCode
from api.handles.home import home_index, carousel_img, course_type,course_up
from api.routes.base import BaseResource
from flask import current_app as app
import logging
home_bp = Blueprint('home', __name__)
api = Api(home_bp)


@api.resource('/index')
class Home(BaseResource):

    def get(self):
        try:
            carousels = carousel_img()
            courses = home_index(page=1, error_out=False)
            course_types = course_type()
            course_tables = course_up()
        except Exception as e:
            raise e
        carousels.update(course_types)
        carousels.update(course_tables)
        carousels.update(courses)
        # app.logger.info('你好')
        # app.logger.error('这是第一个error log')
        # logging.info("你好")
        # logging.debug("你好")
        return {**ErrCode.SUCCESS.value, 'data': carousels}
