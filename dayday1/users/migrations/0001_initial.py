# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(default=b'', max_length=30)),
                ('address', models.CharField(default=b'', max_length=100)),
                ('postcode', models.CharField(default=b'', max_length=20)),
                ('recipient', models.CharField(default=b'', max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userInfo',
            },
        ),
        migrations.CreateModel(
            name='userLogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=30)),
                ('user_passwd', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userLogin',
            },
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(to='users.userLogin'),
        ),
    ]
