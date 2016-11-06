# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user_name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=500)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Course')),
            ],
        ),
    ]