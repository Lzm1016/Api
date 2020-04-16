#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : utils.py
# @Time : 2020/3/9 12:11 PM

import uuid


def uuid_str():
    return '{}'.format(uuid.uuid1())
