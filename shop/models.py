from django.db import models
from FlowerShop import settings

from django.core.validators import MinValueValidator


class TimeInterval(models.Model):
    description = models.CharField(verbose_name='Интервал', max_length=100)

    def __str__(self):
        return self.description


class Holiday(models.Model):
    name = models.CharField(verbose_name='наименование праздника', max_length=300)

    def __str__(self):
        return self.name


class Bouquet(models.Model):
    image = models.ImageField(verbose_name='фото', upload_to='bouquets')
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    description = models.TextField(verbose_name='описание', blank=True)
    consist = models.TextField(verbose_name='состав', blank=True)
    holidays = models.ManyToManyField(Holiday, verbose_name='подходит для праздников:', related_name='bouquets')
    name = models.CharField(verbose_name='Название букета', max_length=30)

    def __str__(self):
        return f'{self.name}_{self.price}'


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


class Aviso(models.Model):
    number = models.IntegerField('номер карты')
    month = models.PositiveSmallIntegerField('месяц окончания действия карты')
    year = models.PositiveSmallIntegerField('год окончания действия карты')
    name = models.CharField('имя владельца карты', max_length=300)
    cvc = models.PositiveSmallIntegerField('cvc карты')
    mail = models.CharField('e-mail', max_length=100, default=None)
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    order = models.ForeignKey(Order, verbose_name='заказ который надо оплатить', on_delete=models.CASCADE,
                              related_name='aviso')

    def __str__(self):
        return f'{self.name}___{self.price}'
