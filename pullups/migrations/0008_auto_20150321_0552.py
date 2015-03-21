# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pullups', '0007_auto_20150320_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 5, 52, 39, 741812)),
            preserve_default=True,
        ),
    ]
