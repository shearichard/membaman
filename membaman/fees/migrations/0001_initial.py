# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_family_organisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('received', models.CharField(max_length=20)),
                ('member', models.ForeignKey(to='members.Member')),
            ],
            options={
                'ordering': ['subyear__start', 'subyear__end'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
            options={
                'ordering': ['start', 'end'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('organisation', models.ForeignKey(to='members.Organisation')),
            ],
            options={
                'ordering': ['start', 'end'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subyear',
            name='year',
            field=models.ForeignKey(to='fees.Year'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='income',
            name='subyear',
            field=models.ForeignKey(to='fees.SubYear'),
            preserve_default=True,
        ),
    ]
