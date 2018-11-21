# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 11:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151014_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationprofile',
            options={
                'permissions':
                (('can_add_project', 'Can add a project to an organization'),
                 ('can_add_xform',
                  'Can add/upload an xform to an organization'),
                 ('view_organizationprofile', 'Can view organization profile'))
            }, ),
    ]