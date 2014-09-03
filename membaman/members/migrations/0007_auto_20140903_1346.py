# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_remove_family_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date_invested',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
    ]
