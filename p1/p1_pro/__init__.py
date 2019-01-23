#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/1/22 21:27
# @Author : Am4zing
# @Site :
# @File : settings.py
# @Software: PyCharm

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

app = Flask('p1_pro')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from p1_pro import views, errors, commands
