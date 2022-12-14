# Generated by Django 4.1.3 on 2022-11-30 10:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0006_alter_realtor_description_alter_realtor_hire_date_and_more'),
        ('listings', '0005_alter_listing_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
        migrations.AddField(
            model_name='listing',
            name='sq_meters',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Площадь в кв.метрах'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Адрес объекта'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Душевые'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(verbose_name='Спальни'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0, verbose_name='Гаражи'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 10, 19, 48, 108827, tzinfo=datetime.timezone.utc), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Площадь участка'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor', verbose_name='Риэлтор'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(max_length=200, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок объявления'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(max_length=200, verbose_name='Почтовый индекс'),
        ),
    ]
