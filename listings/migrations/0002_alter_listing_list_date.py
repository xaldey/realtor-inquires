# Generated by Django 4.1.3 on 2022-11-24 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 24, 19, 29, 43, 471362)),
        ),
    ]