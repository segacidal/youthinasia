# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pullups', '0006_auto_20150320_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 3, 19, 14, 375427)),
            preserve_default=True,
        ),
    ]
