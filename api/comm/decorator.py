#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : decorator.py
# @Time : 2020/3/9 11:40 AM

from datetime import datetime
from functools import wraps


def datetime_str(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        data = fun(*args, **kwargs)
        for k, v in data.items():
            if isinstance(v, datetime):
                data[k] = v.strftime('%Y-%m-%d %H:%M:%S')
        return data

    return wrapper

