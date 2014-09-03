# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20140903_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='sub_organistion',
            new_name='sub_organisation',
        ),
    ]
