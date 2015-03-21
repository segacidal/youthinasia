# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20150217_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 17, 21, 12, 14, 538570), verbose_name=b'date published'),
        ),
    ]
