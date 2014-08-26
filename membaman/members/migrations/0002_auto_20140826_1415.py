# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caregiver',
            options={'ordering': ['name_given', 'name_family']},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['street_address', 'suburb', 'city']},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['name_given', 'name_family']},
        ),
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='suborganisation',
            options={'ordering': ['sub_name']},
        ),
        migrations.AddField(
            model_name='member',
            name='membership_type',
            field=models.CharField(default=b'UK', max_length=2, choices=[(b'KE', b'KE'), (b'CU', b'CU'), (b'SC', b'SC'), (b'VE', b'VE'), (b'UK', b'UK')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='caregiver',
            name='relationship',
            field=models.CharField(default=b'OT', max_length=2, choices=[(b'MO', b'Mother'), (b'FA', b'Father'), (b'GM', b'Grandmother'), (b'GF', b'Grandfather'), (b'SI', b'Sibling'), (b'OT', b'Other')]),
        ),
    ]
