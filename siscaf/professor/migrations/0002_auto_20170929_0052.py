# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='telefone',
            new_name='celular',
        ),
        migrations.AddField(
            model_name='professor',
            name='curso',
            field=models.CharField(max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='sexo',
            field=models.CharField(max_length=15, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='telefoneFixo',
            field=models.CharField(max_length=15, default=10),
            preserve_default=False,
        ),
    ]
