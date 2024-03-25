from django.db import models


class DataInfo(models.Model):
    number = models.IntegerField('Номер чека', max_length=10)
    date = models.DateTimeField('Дата и время')
    price = models.FloatField('Цена', max_length=6)
    product_name = models.CharField('Название товара', max_length=50)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return '/info'

    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'
