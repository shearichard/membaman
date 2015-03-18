# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20150312_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='no_longer_attends',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='no_longer_attends_notification',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
