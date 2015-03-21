# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_remove_image_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='notes',
            field=models.CharField(default=datetime.date(2014, 10, 10), max_length=200),
            preserve_default=False,
        ),
    ]
