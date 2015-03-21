# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pullups', '0002_auto_20150217_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 21, 9, 19, 145707)),
        ),
        migrations.AlterField(
            model_name='pullup',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
