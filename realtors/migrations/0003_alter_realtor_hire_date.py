# Generated by Django 4.1.3 on 2022-11-28 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 11, 28, 16, 42, 16, 139165)),
        ),
    ]
