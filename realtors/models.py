from django.db import models
from django.utils import timezone
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Фото риэлтора"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    is_working = models.BooleanField(
        default=True, verbose_name="Работает в настоящее время?"
    )
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(max_length=100)
    is_mvp = models.BooleanField(default=False, verbose_name="Признак продавца месяца")
    hire_date = models.DateField(
        blank=True, auto_now_add=True, verbose_name="Дата найма"
    )

    def __str__(self):
        return self.name
