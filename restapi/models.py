from django.db import models


class Panty(models.Model):
    product_id = models.IntegerField(primary_key=True, max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField(max_length=10)
    img = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=50)
    stock = models.IntegerField(max_length=10, verbose_name="Cantidad Disponible")

    def __str__(self):
        return self.name