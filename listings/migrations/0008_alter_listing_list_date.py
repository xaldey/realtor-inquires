# Generated by Django 4.1.3 on 2022-11-30 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_alter_listing_list_date_alter_listing_sq_meters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 11, 25, 58, 714030, tzinfo=datetime.timezone.utc), verbose_name='Дата публикации'),
        ),
    ]
