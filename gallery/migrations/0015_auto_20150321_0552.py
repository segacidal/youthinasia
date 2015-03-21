# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20150320_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 21, 5, 52, 39, 740780), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
