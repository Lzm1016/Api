#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : config.py
# @Time : 2020/3/6 5:25 PM


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_NAME = 'wxapi'
    LOG_FILENAME = './log/wx.log'
    LOG_MAXBYTES = 1000000
    LOG_BACKUPCOUNT = 4
    LOG_FORMATTER = "%(asctime)s : %(filename)s - %(funcName)s - [line:%(lineno)d] - %(levelname)s - %(message)s"

    @classmethod
    def get(cls, key, default):
        try:
            return getattr(cls, key)
        except Exception:
            return default


class DevelopmentConfig(Config):
    DEBUG = True

    # 数据库 配置
    BD_USERNAME = 'root'
    BD_PASSWORD = 'Lzm123456'
    BD_HOST = 'localhost'
    BD_PORT = '3306'
    BD_NAME = 'api'
    CHARSET = 'utf8mb4'
    # 数据驱动
    DB_URI = f'mysql+pymysql://{BD_USERNAME}:{BD_PASSWORD}@{BD_HOST}:{BD_PORT}/{BD_NAME}?charset={CHARSET}'
    SQLALCHEMY_DATABASE_URI = DB_URI


class Production(Config):
    pass


config = {
    'default': DevelopmentConfig,
    'production': Production
}
