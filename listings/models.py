from django.utils import timezone
from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(
        Realtor, on_delete=models.DO_NOTHING, verbose_name="Риэлтор"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок объявления")
    address = models.CharField(max_length=200, verbose_name="Адрес объекта")
    city = models.CharField(max_length=200, verbose_name="Город")
    state = models.CharField(max_length=200, verbose_name="Регион")
    zipcode = models.CharField(max_length=200, verbose_name="Почтовый индекс")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    bedrooms = models.IntegerField(verbose_name="Спальни")
    bathrooms = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name="Душевые"
    )
    garage = models.IntegerField(default=0, verbose_name="Гаражи")
    sq_meters = models.DecimalField(
        default=0,
        verbose_name="Площадь в кв.метрах",
        blank=True,
        decimal_places=2,
        max_digits=7,
    )
    lot_size = models.DecimalField(
        max_digits=5, decimal_places=1, verbose_name="Площадь участка"
    )
    photo_main = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name="Главное фото"
    )
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(
        default=timezone.now(), verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title
