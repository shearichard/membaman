# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0007_referencemapper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountpayment',
            name='description',
            field=models.CharField(max_length=128, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='referencemapper',
            name='payment_reference_used',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
