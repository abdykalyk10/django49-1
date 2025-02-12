from django.db import models

class ClothingCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Clothes(models.Model):
    title = models.CharField(max_length=100, verbose_name='названия одежды')
    price = models.FloatField(default=300, verbose_name='укажите ценну')
    clothing_category = models.ManyToManyField(ClothingCategory)

    def __str__(self):
        return self.title


