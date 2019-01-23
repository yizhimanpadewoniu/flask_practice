#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/23 9:21 
# @Author : Am4zing
# @Site :  
# @File : errors.py 
# @Software: PyCharm

from flask import render_template
from p1_pro import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
