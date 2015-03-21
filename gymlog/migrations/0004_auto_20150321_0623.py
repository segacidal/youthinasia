# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gymlog', '0003_auto_20150321_0552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 6, 23, 57, 520075)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 6, 23, 57, 520464)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 6, 23, 57, 521338)),
            preserve_default=True,
        ),
    ]
