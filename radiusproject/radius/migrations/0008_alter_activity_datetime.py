# Generated by Django 3.2.8 on 2021-11-09 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radius', '0007_auto_20211109_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 21, 20, 38, 294920)),
        ),
    ]
