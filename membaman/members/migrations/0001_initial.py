# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caregiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_given', models.CharField(max_length=50, verbose_name=b'given name')),
                ('name_family', models.CharField(max_length=50, verbose_name=b'family name')),
                ('phone_mobile', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=2, choices=[(b'MO', b'Mother'), (b'FA', b'Father'), (b'GM', b'Grandmother'), (b'GF', b'Grandfather'), (b'SI', b'Sibling'), (b'OT', b'Other')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_address', models.CharField(max_length=75)),
                ('suburb', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('phone_fixed', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_given', models.CharField(max_length=50, verbose_name=b'given name')),
                ('name_family', models.CharField(max_length=50, verbose_name=b'family name')),
                ('date_of_birth', models.DateField()),
                ('date_invested', models.DateField()),
                ('caregivers', models.ManyToManyField(related_name=b'caregivers', to='members.Caregiver')),
                ('family', models.ForeignKey(to='members.Family')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubOrganisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_name', models.CharField(max_length=50)),
                ('organistion', models.ForeignKey(to='members.Organisation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='organistion',
            field=models.ForeignKey(to='members.Organisation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='primary_caregiver',
            field=models.ForeignKey(related_name=b'primary_caregiver', to='members.Caregiver'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='sub_organistion',
            field=models.ForeignKey(to='members.SubOrganisation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caregiver',
            name='family',
            field=models.ForeignKey(to='members.Family'),
            preserve_default=True,
        ),
    ]
