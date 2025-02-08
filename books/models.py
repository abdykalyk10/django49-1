from django.db import models
from django.db.models import CharField, EmailField


class BookModel(models.Model):
    GENER_CHOICES = (
        ('HORROR', "HORROR"),
        ('COMEDY', "COMEDY"),
        ('FANTASY', "FANTASY"),
    )
    image = models.ImageField(upload_to="books/", verbose_name="загрузите фото")
    title = models.CharField(max_length=100, verbose_name='укажите названия книги')
    description = models.TextField(verbose_name='укажите описания книги', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=200)
    created_at = models.DateField(auto_now_add=True)
    genre = CharField(max_length=10, choices=GENER_CHOICES, default='HORROR',
                      verbose_name='выберите жаныр')
    email = EmailField(max_length=100,verbose_name='укажите почту')
    director = models.CharField(max_length=100, default='Иванов Иван')
    audio = models.URLField(verbose_name='укажите ссылку из YOUTUBE')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'