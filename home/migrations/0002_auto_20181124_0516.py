# Generated by Django 2.1.3 on 2018-11-24 05:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 5, 16, 8, 835173, tzinfo=utc)),
        ),
    ]
