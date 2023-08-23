from django.db import models
from FlowerShop import settings
from pathlib import Path
# from datetime import datetime
# from phonenumber_field.modelfields import PhoneNumberField


class Bouquet(models.Model):
    image = models.ImageField(verbose_name='фото', upload_to='bouquets')
    price = models.FloatField(verbose_name='цена')
    def __str__(self):
        return f'{self.id}_{self.price}'

class Order(models.Model):
    bouquet = models.ForeignKey(Bouquet, verbose_name='букет', related_name='orders', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=300)
    phone = models.CharField(verbose_name='телефон', max_length=300)
    address = models.CharField(verbose_name='адрес', max_length=300)
    period = models.PositiveSmallIntegerField(verbose_name='время доставки', choices=settings.PERIOD, default=1)

    def __str__(self):
        return f'{self.name}_{self.bouquet.price}'


