# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(default=None, blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
    ]
