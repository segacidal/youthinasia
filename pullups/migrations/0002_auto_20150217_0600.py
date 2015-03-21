# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pullups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 2, 17, 6, 0, 20, 109970)),
        ),
        migrations.AlterField(
            model_name='pullup',
            name='notes',
            field=models.TextField(),
        ),
    ]
