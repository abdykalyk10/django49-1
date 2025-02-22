from django.db import models

class CarModel(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=100)
    counters = models.TextField()
    like = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)

    def __str__(self):

        return f"{self.title} - {self.price}, {self.city}, Лайков: {self.like}, {self.counters}"
class RezkaModel(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title}"