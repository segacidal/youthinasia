# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20150215_0628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='image',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 6, 57, 50, 770654), verbose_name=b'date published'),
        ),
    ]
