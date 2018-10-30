# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-20 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_quotes', to='login_app.User'),
        ),
    ]