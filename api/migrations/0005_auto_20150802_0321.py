# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150802_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='producer',
            new_name='owner',
        ),
    ]
