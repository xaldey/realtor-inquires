from django.db import models
from django.utils import timezone


class Developer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование застройщика")
    type_of_organization = models.CharField(
        max_length=50, verbose_name="Вид организации", blank=True
    )
    inn_organization = models.IntegerField(
        verbose_name="ИНН организации",
        blank=True,
    )
    city_main_location = models.CharField(
        max_length=100, verbose_name="Город расположения офиса", blank=True
    )
    description = models.TextField(verbose_name="Описание компании")
    web_site = models.CharField(
        blank=True, max_length=255, verbose_name="Сайт компании"
    )
    logo = models.ImageField(
        blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Логотип компании"
    )
    is_working = models.BooleanField(
        default=True, verbose_name="Работает в настоящий момент?"
    )
    is_holding_member = models.BooleanField(
        default=True, verbose_name="Входит в холдинг ВКБ?"
    )

    def __str__(self):
        return self.name
