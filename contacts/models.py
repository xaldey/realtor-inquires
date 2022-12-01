from django.db import models
from datetime import datetime


class Contact(models.Model):
    listing = models.CharField(max_length=200, verbose_name="Объявление")
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200, verbose_name="Имя контакта")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    message = models.TextField(blank=True, verbose_name="Сообщение")
    contact_date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name="Дата обращения"
    )
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
