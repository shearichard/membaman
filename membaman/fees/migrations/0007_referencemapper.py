# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0006_auto_20150320_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceMapper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('payment_reference_used', models.CharField(max_length=10)),
                ('payment_reference_intended', models.CharField(max_length=10)),
                ('payment_origination_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
