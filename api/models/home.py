#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : home.py
# @Time : 2020/3/6 5:49 PM

from api.comm.utils import uuid_str
from .base import db, BaseModel, db_session


class CourseModel(db.Model, BaseModel):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(255), default=uuid_str())
    course_name = db.Column(db.String(255))
    chapter_name = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    course_type_id = db.Column(db.SmallInteger)
    course_type_name = db.Column(db.String(255))
    description = db.Column(db.Text)
    video_url = db.Column(db.String(255))

    # video_duration = db.Column(db.String(64))


class CourseTypeModel(db.Model, BaseModel):
    __tablename__ = 'course_type'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(500), default=uuid_str())
    # course_type = db.Column(db.String(255))
    course_type_name = db.Column(db.String(255))
    bg_image = db.Column(db.String(255))


class AddCoursesModel(db.Model, BaseModel):
    __tablename__ = 'newcourses'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(500), default=uuid_str())
    name = db.Column(db.String(255))
    chapters = db.Column(db.String(255))
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    upclass_times = db.Column(db.String(255))
    course_duration = db.Column(db.Integer)
    sign_in = db.Column(db.Integer)
    sigin_address = db.Column(db.String(255))
    address_latitude = db.Column(db.String(255))
    sign_range = db.Column(db.Integer)
