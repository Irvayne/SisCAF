# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_auto_20170922_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='telefone',
            new_name='celular',
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='sexo',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefoneFixo',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
