# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pullup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_set', models.IntegerField()),
                ('second_set', models.IntegerField()),
                ('third_set', models.IntegerField()),
                ('average', models.FloatField()),
                ('time_of_day', models.CharField(max_length=1, choices=[(b'M', b'Morning'), (b'D', b'Day'), (b'N', b'Night')])),
                ('date', models.DateField(default=datetime.datetime(2015, 2, 17, 5, 45, 4, 574187))),
                ('notes', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
