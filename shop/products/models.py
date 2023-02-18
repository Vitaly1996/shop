from django.db import models
from django.conf import settings

class Item(models.Model):
    conv_cent_usd = 100
    name = models.CharField(max_length=100, verbose_name='Название_товара')
    price = models.IntegerField (default=0, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return '{0:.2f}'.format(self.price/settings.CONV_CENT_USD)