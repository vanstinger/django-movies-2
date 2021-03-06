# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lensview', '0013_auto_20160507_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='occupation',
            field=models.IntegerField(choices=[(0, 'Other'), (1, 'Academic/Educator'), (2, 'Artist'), (3, 'Clerical/Admin'), (4, 'College/Grad Student'), (5, 'Customer Service'), (6, 'Doctor/Health Care'), (7, 'Executive/Managerial'), (8, 'Farmer'), (9, 'Homemaker'), (10, 'K-12 Student'), (11, 'Lawyer'), (12, 'Programmer'), (13, 'Retired'), (14, 'Sales/Marketing'), (15, 'Scientist'), (16, 'Self-employed'), (17, 'Technician/Engineer'), (18, 'Tradesman/Craftsman'), (19, 'Unemployed'), (20, 'Writer')]),
        ),
    ]
