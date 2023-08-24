from django.db import models
from FlowerShop import settings


class Holiday(models.Model):
    name = models.CharField(verbose_name='наименование праздника', max_length=300)

    def __str__(self):
        return self.name


class Bouquet(models.Model):
    image = models.ImageField(verbose_name='фото', upload_to='bouquets')
    price = models.FloatField(verbose_name='цена')
    description = models.TextField(verbose_name='описание', blank=True)
    consist = models.TextField(verbose_name='состав', blank=True)
    holidays = models.ManyToManyField(Holiday, verbose_name='подходит для праздников:')

    def __str__(self):
        return f'{self.pk}_{self.price}'


class Order(models.Model):
    bouquet = models.ForeignKey(Bouquet, verbose_name='букет', related_name='orders', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=300)
    phone = models.CharField(verbose_name='телефон', max_length=300)
    address = models.CharField(verbose_name='адрес', max_length=300)
    period = models.PositiveSmallIntegerField(verbose_name='время доставки', choices=settings.PERIOD, default=1)

    def __str__(self):
        return f'{self.name}_{self.bouquet.price}'


class Consulting(models.Model):
    name = models.CharField(verbose_name='имя', max_length=300)
    phone = models.CharField(verbose_name='телефон', max_length=300)

    def __str__(self):
        return f'{self.name}_{self.phone}'
