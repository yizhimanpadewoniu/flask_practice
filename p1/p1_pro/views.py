#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/23 9:21 
# @Author : Am4zing
# @Site :  
# @File : views.py 
# @Software: PyCharm

from flask import flash, redirect, url_for, render_template

from p1_pro import app, db
from p1_pro.forms import HelloForm
from p1_pro.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        messages = Message(body=body, name=name)
        db.session.add(messages)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
