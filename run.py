#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : run.py
# @Time : 2020/4/16 5:06 PM


import subprocess as sub

cmd = ['gunicorn', '-c', 'conf.py', 'app:app']
sub.run(cmd)
