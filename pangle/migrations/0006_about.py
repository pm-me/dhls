# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-07-26 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pangle', '0005_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
            ],
            options={
                'verbose_name': '\u5173\u4e8e',
                'verbose_name_plural': '\u5173\u4e8e',
            },
        ),
    ]
