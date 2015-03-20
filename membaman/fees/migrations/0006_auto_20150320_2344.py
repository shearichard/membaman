# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0005_auto_20150320_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountentry',
            name='amount',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
