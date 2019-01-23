#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/1/22 21:27
# @Author : Am4zing
# @Site :
# @File : settings.py
# @Software: PyCharm

import os
from p1_pro import app


dev_db = "mysql+pymysql://root:root@192.168.1.117/data"

SECRET_KEY = os.getenv('SECRET_KEY', 'afsdfasdfasdfasdfasdfasdfasdf')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
