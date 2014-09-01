# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subyear',
            options={'ordering': ['year__organisation__name', 'start', 'end']},
        ),
        migrations.AlterField(
            model_name='income',
            name='received',
            field=models.CharField(max_length=50),
        ),
    ]
