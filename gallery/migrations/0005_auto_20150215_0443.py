# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_gallery_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='gallery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 4, 43, 10, 477080), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
