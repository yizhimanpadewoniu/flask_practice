#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/23 9:15 
# @Author : Am4zing
# @Site :  
# @File : models.py 
# @Software: PyCharm


from datetime import datetime
from p1_pro import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
