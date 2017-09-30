# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_auto_20170922_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='turma',
            field=models.CharField(default=10, max_length=255),
            preserve_default=False,
        ),
    ]
