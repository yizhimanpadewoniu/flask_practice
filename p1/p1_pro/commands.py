#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/23 10:25 
# @Author : Am4zing
# @Site :  
# @File : commands.py 
# @Software: PyCharm

import click

from p1_pro import app, db
from p1_pro.models import Message


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        click.confirm('delete the database.')
        db.drop_all()
        click.echo('Drop tables')
    db.create_all()
    click.echo('Init success')


@app.cli.command()
@click.option('--count', default=20, help='default is 20')
def forge(count):
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('Working...')

    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)

    db.session.commit()
    click.echo('Create %d fake messages.' % count)
