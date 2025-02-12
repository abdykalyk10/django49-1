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
    music = models.FileField(upload_to='music/', verbose_name='загрузите музыку', null=True, blank=True)
    audio = models.URLField(verbose_name='укажите ссылку из YOUTUBE')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

class Review(models.Model):
    STARS = (
        ('🌟', '🌟'),
        ('🌟🌟', '🌟🌟'),
        ('🌟🌟🌟', '🌟🌟🌟'),
        ('🌟🌟🌟🌟', '🌟🌟🌟🌟'),
        ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟🌟'),
    )
    choice_book = models.ForeignKey(BookModel, on_delete=models.CASCADE,
                                    related_name='choice_book')
    created_at = models.DateField(auto_now_add=True)

    text_review = models.TextField(default='Крутой фильм')
    stars = models.CharField(max_length=10, choices=STARS, default='🌟🌟🌟')
    def __str__(self):
        return f'{self.stars}--{self.choice_book.title}'
