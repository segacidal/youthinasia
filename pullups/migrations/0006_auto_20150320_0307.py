# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import pullups.models


class Migration(migrations.Migration):

    dependencies = [
        ('pullups', '0005_auto_20150221_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 3, 7, 33, 303179)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pullup',
            name='first_set',
            field=models.IntegerField(validators=[pullups.models.is_positive]),
            preserve_default=True,
        ),
    ]
