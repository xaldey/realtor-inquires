# Generated by Django 4.1.3 on 2022-12-06 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_listing_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 16, 6, 59, 978182, tzinfo=datetime.timezone.utc), verbose_name='Дата публикации'),
        ),
    ]
