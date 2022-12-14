# Generated by Django 4.1.3 on 2022-12-14 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_alter_contact_phone_alter'),
        ('developers', '0014_alter_developer_city_main_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='director',
            field=models.ForeignKey(blank=True, null=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Руководитель', to='contacts.contact'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='inn_organization',
            field=models.CharField(blank=True, max_length=20, null=None, verbose_name='ИНН организации'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Логотип компании'),
        ),
        migrations.AlterField(
            model_name='developer',
            name='type_of_organization',
            field=models.CharField(choices=[('ООО', 'ООО'), ('ООО СЗ', 'ООО СЗ'), ('ООО ИСК', 'ООО ИСК'), ('ООО УК', 'ООО УК'), ('АО', 'АО'), ('ЗАО', 'ЗАО'), ('ОАО', 'ОАО'), ('ИП', 'ИП')], default='ООО', max_length=30),
        ),
    ]