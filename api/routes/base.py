#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : base.py
# @Time : 2020/3/9 10:25 AM

from flask_restful import Resource
from flask_restful.reqparse import RequestParser


class BaseResource(Resource, RequestParser):
    def __init__(self):
        super().__init__()
