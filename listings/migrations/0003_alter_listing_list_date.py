# Generated by Django 4.1.3 on 2022-11-28 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 28, 16, 42, 16, 140033)),
        ),
    ]
