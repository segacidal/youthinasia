# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gymlog.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateField(default=datetime.datetime(2015, 3, 20, 3, 7, 33, 303824))),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateField(default=datetime.datetime(2015, 3, 20, 3, 7, 33, 304193))),
                ('slug', models.SlugField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.FloatField()),
                ('reps', models.IntegerField(validators=[gymlog.models.is_positive])),
                ('sets', models.IntegerField(validators=[gymlog.models.is_positive])),
                ('date', models.DateField(default=datetime.datetime(2015, 3, 20, 3, 7, 33, 304582))),
                ('exercise', models.ForeignKey(to='gymlog.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
