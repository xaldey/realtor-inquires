from django.db import models

from contacts.models import Contact


class Developer(models.Model):

    name = models.CharField(max_length=255, verbose_name="Наименование застройщика")

    OOO = "ООО"
    OOOSZ = "ООО СЗ"
    OOOISK = "ООО ИСК"
    OOOUK = "ООО УК"
    AO = "АО"
    ZAO = "ЗАО"
    OAO = "ОАО"
    IP = "ИП"

    TYPE_OF_ORG = [
        (OOO, "ООО"),
        (OOOSZ, "ООО СЗ"),
        (OOOISK, "ООО ИСК"),
        (OOOUK, "ООО УК"),
        (AO, "АО"),
        (ZAO, "ЗАО"),
        (OAO, "ОАО"),
        (IP, "ИП"),
    ]

    type_of_organization = models.CharField(
        choices=TYPE_OF_ORG, default=OOO, max_length=30
    )
    inn_organization = models.CharField(
        max_length=20,
        verbose_name="ИНН организации",
        blank=True,
        null=None,
    )

    director = models.ForeignKey(
        Contact,
        related_name="Руководитель",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=None,
    )

    city_main_location = models.CharField(
        max_length=100, verbose_name="Город расположения головного офиса", blank=True
    )
    description = models.TextField(verbose_name="Описание компании")
    web_site = models.CharField(
        blank=True, max_length=255, verbose_name="Сайт компании"
    )
    logo = models.ImageField(
        blank=True,
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Логотип компании",
        null=True,
    )
    is_working = models.BooleanField(
        default=True, verbose_name="Работает в настоящий момент?"
    )
    is_holding_member = models.BooleanField(
        default=True, verbose_name="Входит в холдинг ВКБ?"
    )

    def __str__(self):
        return self.name
