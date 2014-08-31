# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_family_organisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='organisation',
        ),
    ]
