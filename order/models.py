from tabnanny import verbose

from django.db import models
from books.models import BookModel

class OrderModel(models.Model):
    STATUS_CHOICES = (
        ('Прочитано', 'Прочитано'),
        ('Не прочитано','Не прочитано')
    )
    task = models.CharField(max_length=120)
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    choice_status = models.CharField(max_length=120, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
