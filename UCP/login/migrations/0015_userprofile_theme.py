# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20160707_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='theme',
            field=models.CharField(default=b'cerulean', max_length=10, choices=[(b'cerulean', b'cerulean'), (b'flat', b'flat')]),
        ),
    ]
