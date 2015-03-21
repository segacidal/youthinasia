# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20150215_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 17, 5, 45, 4, 571694), verbose_name=b'date published'),
        ),
    ]
