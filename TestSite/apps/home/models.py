from django.db import models

class Product(models.Model):
    title = models.CharField('название товара', max_length=170)
    description = models.TextField('описание товара', max_length=500)
    price = models.IntegerField('цена товара')

    def __str__(self):
        return self.title
    
    def WasProfitable(self):
        return self.price <= 500
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'