# Generated by Django 4.1.3 on 2022-12-10 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_remove_contact_user_id'),
        ('developers', '0009_alter_developer_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='director',
        ),
        migrations.AddField(
            model_name='developer',
            name='director_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.contact', verbose_name='Руководитель предприятия'),
        ),
    ]
