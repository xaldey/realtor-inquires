# Generated by Django 4.1.3 on 2022-12-07 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0004_alter_developer_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='city_main_location',
            field=models.CharField(blank=True, max_length=100, verbose_name='Город расположения офиса'),
        ),
    ]
