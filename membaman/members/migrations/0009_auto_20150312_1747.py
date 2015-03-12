# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20140903_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caregiver',
            options={'ordering': ['name_family', 'name_given']},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['name_family', 'name_given']},
        ),
        migrations.AddField(
            model_name='organisation',
            name='bank_account_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organisation',
            name='bank_account_number',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
