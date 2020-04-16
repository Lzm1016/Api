#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : base.py.py
# @Time : 2020/3/9 9:57 AM


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from api.comm.decorator import datetime_str

db = SQLAlchemy()
db_session = db.session


class BaseModel(object):
    created_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

    @property
    @datetime_str
    def to_dict(self):
        return {col.name: getattr(self, col.name, None) for col in self.__table__.columns}
