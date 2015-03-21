# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pullups', '0004_auto_20150217_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullup',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pullup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 2, 21, 5, 40, 1, 314328)),
        ),
    ]
