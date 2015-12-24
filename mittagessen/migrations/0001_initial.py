# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Essen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('category_name', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Esser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('alias', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('bill', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mittagessen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(default=0)),
                ('date', models.DateField()),
                ('person', models.ForeignKey(to='mittagessen.Esser')),
                ('type', models.ForeignKey(to='mittagessen.Essen')),
            ],
        ),
    ]
