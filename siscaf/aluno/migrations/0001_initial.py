# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cpf', models.CharField(max_length=15)),
                ('rg', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
