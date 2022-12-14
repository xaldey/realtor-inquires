# Generated by Django 4.1.3 on 2022-12-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_phone_alter_alter_contact_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_alter',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
