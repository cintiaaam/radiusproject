# Generated by Django 3.2.8 on 2021-11-09 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radius', '0006_auto_20211106_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default='noimage.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 20, 12, 17, 465006)),
        ),
    ]
