# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20150215_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(default='defaultslug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='thumb',
            field=models.CharField(default='defaultthumb', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 15, 6, 28, 6, 104669), verbose_name=b'date published'),
        ),
    ]
