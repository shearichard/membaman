# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0003_auto_20140903_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'ordering': ['member__name_family', 'member__name_given', 'subyear__start', 'subyear__end']},
        ),
    ]
