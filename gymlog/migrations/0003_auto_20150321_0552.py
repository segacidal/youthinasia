# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gymlog', '0002_auto_20150320_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='name',
            field=models.CharField(max_length=50, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 5, 52, 39, 743142)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 5, 52, 39, 743518)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 21, 5, 52, 39, 744402)),
            preserve_default=True,
        ),
    ]
