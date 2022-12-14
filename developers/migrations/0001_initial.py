# Generated by Django 4.1.3 on 2022-12-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование застройщика')),
                ('type_of_organization', models.CharField(blank=True, max_length=50, verbose_name='Вид организации')),
                ('inn_organization', models.IntegerField(blank=True, verbose_name='ИНН организации')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Логотип компании')),
                ('is_working', models.BooleanField(default=True)),
            ],
        ),
    ]
