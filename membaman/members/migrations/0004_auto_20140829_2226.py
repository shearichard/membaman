# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20140826_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='organistion',
            new_name='organisation',
        ),
        migrations.RenameField(
            model_name='suborganisation',
            old_name='organistion',
            new_name='organisation',
        ),
    ]
