# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_auto_20150318_2331'),
        ('fees', '0004_auto_20150312_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=3, decimal_places=2)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AccountDebt',
            fields=[
                ('accountentry_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fees.AccountEntry')),
                ('invoice_reference', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=('fees.accountentry',),
        ),
        migrations.CreateModel(
            name='AccountPayment',
            fields=[
                ('accountentry_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fees.AccountEntry')),
                ('payment_type', models.CharField(default=b'OT', max_length=2, choices=[(b'AT', b'Automated Payment'), (b'TR', b'Bank Transfer'), (b'CA', b'Cash'), (b'CH', b'Credit'), (b'DI', b'Discount'), (b'OT', b'Other')])),
                ('payment_reference', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=10, null=True, blank=True)),
                ('notes', models.CharField(max_length=128, null=True, blank=True)),
            ],
            options={
            },
            bases=('fees.accountentry',),
        ),
        migrations.AddField(
            model_name='accountentry',
            name='member',
            field=models.ForeignKey(to='members.Member'),
            preserve_default=True,
        ),
    ]
