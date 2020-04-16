#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Author : Liu
# @FileName : home.py
# @Time : 2020/3/9 4:27 PM

from api.models.base import db_session
from api.models.home import CourseModel, CourseTypeModel, AddCoursesModel


def home_index(page=1, per_page=10, error_out=True):
    courses = CourseModel.query.paginate(page, per_page, error_out)

    all_course = []
    for item in courses.items:
        all_course.append(item.to_dict)

    return {'courses': all_course, 'current_page': courses.page, 'pages': courses.pages, 'per_page': courses.per_page,
            'has_next': courses.has_next}


def carousel_img():
    course = db_session.query(CourseModel.course_type_id, CourseModel.image_url).group_by(CourseModel.course_type_id,
                                                                                          CourseModel.image_url).all()
    courses = []
    for k, v in course:
        courses.append({
            'id': k,
            'img_url': v
        })

    return {'carousel': courses}


def course_type():
    types = CourseTypeModel.query.all()
    course_type = []
    for type in types:
        course_type.append(type.to_dict)

    return {'course_types': course_type}


def course_up():
    courses = AddCoursesModel.query.all()
    up_course = []
    for cou in courses:
        up_course.append(cou.to_dict)

    return {'up_course': up_course}
