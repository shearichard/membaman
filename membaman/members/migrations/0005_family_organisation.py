# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20140829_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='organisation',
            field=models.ForeignKey(default=1, to='members.Organisation'),
            preserve_default=False,
        ),
    ]
