from django.db import models
from datetime import datetime


class Lead(models.Model):
    """
    Лид создается при первом контакте потенциального клиента.
    Каждый лид хочет стать контактом, а потом довольным клиентом, совершившим покупку.
    """

    name = models.CharField(max_length=200, verbose_name="Имя лида при контакте")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    message = models.TextField(blank=True, verbose_name="Сообщение")
    contact_tstamp = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name="Дата обращения"
    )
    edited_tstamp = models.DateTimeField(
        auto_now=True, verbose_name="Последние исправления"
    )

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    Контакт - клиент, о котором мы узнали что-то больше чем телефон и имя.
    Он мог раньше быть "лидом", а мог сразу быть контактом.
    """

    name = models.CharField(max_length=200, verbose_name="Имя контакта")
    first_name = models.CharField(
        verbose_name="Имя контакта", max_length=50, blank=True
    )
    patronym_name = models.CharField(
        verbose_name="Отчество контакта", max_length=50, blank=True
    )
    last_name = models.CharField(
        verbose_name="Фамилия контакта", max_length=50, blank=True
    )

    date_of_birth = models.DateField(
        default=None, blank=True, verbose_name="Дата рождения контакта"
    )

    listing = models.CharField(max_length=200, verbose_name="Объявление", blank=True)
    listing_id = models.IntegerField(blank=True)

    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, verbose_name="Телефон", blank=True)
    phone_alter = models.CharField(
        max_length=50, verbose_name="Телефон", default=None, blank=True
    )
    message = models.TextField(blank=True, verbose_name="Сообщение")
    contact_date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Дата обращения"
    )
    user_id = models.IntegerField(blank=True, default=None)

    def __str__(self):
        return self.name
