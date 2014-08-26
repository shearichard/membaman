# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20140826_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='membership_type',
            field=models.CharField(default=b'UK', max_length=2, choices=[(b'KE', b'Kea'), (b'CU', b'Cub'), (b'SC', b'Scout'), (b'VE', b'Venturer'), (b'UK', b'Unknown')]),
        ),
    ]
