#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : errcode_enum.py
# @Time : 2020/4/7 4:01 PM

from enum import Enum, unique


@unique
class ErrCode(Enum):

    SUCCESS = {
        'errcode': 1000,
        'msg': '请求成功'
    }
    ACCOUNT_ERROR = {
        'errcode': 1001,
        'msg': '账号密码错误'
    }
    PARAM_NO_NUll = {
        'errcode': 1003,
        'msg': '参数不能为空'
    }

    PARAM_INVALID_ERROR = {
        'errcode': 1004,
        'msg': '参数错误'
    }

