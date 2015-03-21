# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gymlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exercise',
            name='days',
            field=models.ManyToManyField(to='gymlog.Day'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 3, 19, 14, 376325)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day',
            name='slug',
            field=models.SlugField(editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 3, 19, 14, 376711)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='slug',
            field=models.SlugField(editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='instance',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 3, 20, 3, 19, 14, 377553)),
            preserve_default=True,
        ),
    ]
